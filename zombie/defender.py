import random
import agentsim
from person import Person
from moveenhanced import MoveEnhanced

# Design note:
# The only reason for importing zombie and normal is to allow the class queries
# for zombies, normals such as
#   zombie.Zombie.get_all_instances()
# 
# If we used the import form:
#   from zombie import Zombie
# we would say
#   Zombie.get_all_instances()
# but this won't work because circular references would be created among 
# the three subclasses Zombies, Normals, and Defenders.  That is, the three
# classes are co-dependent in that they need to know that each other exists.

# The proper solution is that zombie, normal, defender would all be placed
# in the same module file to achieve the co-dependencies without the import.  
# But we want them in different files for the tournament.  There is never
# a good pure solution in the real world.

import zombie
import normal

class Defender(MoveEnhanced):
    """
    Goes around attempting to prevent zombies form reaching normals
    """

    def __init__(self, **keywords):
        MoveEnhanced.__init__(self, **keywords)

        if agentsim.debug.get(2):
            print("Defender", self._name)

    def get_author(self):
        return "Adam Ford"

    def compute_next_move(self):
        delta_x = 0
        delta_y = 0
        overlapping = False

        # check if we're overlapping with anyone and move off
        # no need to check for zombies as we'll just teleport them instead

        defenders = Defender.get_all_present_instances()
        normals = normal.Normal.get_all_present_instances()

        non_zombies = defenders + normals

        if len(non_zombies) > 1:
            nearest = min(
                # make pairs of (person, distance from self to person)
                [ (p, self.distances_to(p) ) for p in non_zombies if p.get_id() != self.get_id()]
                ,
                # and sort by edge-to-edge distance
                key=(lambda x: x[1][3])
                )

            (d, delta_x, delta_y, d_edge_edge) = nearest[1]

            if d > 0 and d_edge_edge < 0:
                # Means we're overlapping with the nearest person
                # Let's move directly away from them
                overlapping = True

                # move in exactly the opposite direction of person
                # with which we're overlapping but move maximum
                # distance allowed
                # We'll still be stuck if move_limit isn't far enough
                # to fix overlap
                move_limit = self.get_move_limit()
                delta_x = -delta_x * (move_limit/d)
                delta_y = -delta_y * (move_limit/d)

        if not overlapping:
            # find nearest zombie if there is one!
            all_z = zombie.Zombie.get_all_present_instances()
            if all_z:
                nearest = min(
                    # make pairs of (person, distance from self to person)
                    [ (z, self.distances_to(z)[0] ) for z in all_z ]
                    ,
                    # and sort by distance
                    key=(lambda x: x[1])
                    )

                (near_z, near_d) = nearest

                # move towards nearest zombie
                (d, delta_x, delta_y, d_edge_edge) = self.distances_to(near_z)

                if agentsim.debug.get(64):
                    print("nearest zombie to {} is {}, dx {} dy {}".format(
                        self.get_name(), near_z.get_name(), delta_x, delta_y, d_edge_edge))

                d_edge_edge = round(d_edge_edge, 3)

                # but if close enough to teleport, send the zombie to a random
                # point instead
                if d_edge_edge <= self.get_teleport_threshold() :
                    (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
                    x = random.randint(x_min, x_max)
                    y = random.randint(y_min, y_max)
                    self.teleport(near_z, x, y)

                if self.get_move_limit() > d_edge_edge:
                    # if the distance between my edge and the target's edge is smaller than
                    # the move limit, need to reduce delta_x and delta_y so we go right to
                    # edge

                    delta_x = delta_x * d_edge_edge/d
                    delta_y = delta_y * d_edge_edge/d

                # and change happiness proportional to distance
                (w,h) = agentsim.gui.get_canvas_size()
                diag = (w*w + h*h) ** .5
                delta_h = min( d/diag, .05)
                if agentsim.debug.get(64):
                    print("d", d, "diag", diag, "dh", delta_h)

                self.set_happiness(delta_h + self.get_happiness())

        # alert the normals
        for n in normal.Normal.get_all_present_instances():
            n.zombie_alert(0, 0)

        return (delta_x, delta_y)

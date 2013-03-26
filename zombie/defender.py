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
    Goes around attempting to prevent zombies from reaching normals
    """

    _normal_corner = None
    _zombie_corner = None

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

        # First, find all zombies within teleporting range and get 'em outta here
        all_z = zombie.Zombie.get_all_present_instances()
        if all_z:
            zombies_with_range = [ (z, self.distances_to(z)) for z in all_z ]
            zombies_in_range = [ t for t in zombies_with_range if round(t[1][3],3) <= self.get_teleport_threshold() ]

            for t in zombies_in_range:
                (near_z, distances) = t
                (d, delta_x, delta_y, d_edge_edge) = distances

                d_edge_edge = round(d_edge_edge, 3)

                corner = Defender._zombie_corner
                (corner_x, corner_y) = corner
                x_descending = corner_x != 0
                y_descending = corner_y != 0

                range_x = 0
                range_y = 0

                # Keep trying to teleport the zombie near the desired corner until it actually sticks
                # The range increases with each attempt
                # This construct somewhat emulates a C do...while loop
                # Will stop after X amount of loops to prevent an infinite one
                while True:
                    x = random.randint(corner_x - range_x, corner_x) if x_descending else random.randint(corner_x, corner_x + range_x)
                    y = random.randint(corner_y - range_y, corner_y) if y_descending else random.randint(corner_y, corner_y + range_y)
                    self.teleport(near_z, x, y)

                    if round(self.distances_to(near_z)[3],3) > self.get_teleport_threshold() or range_x > 250:
                        break
                    else:
                        range_x = range_x + 5
                        range_y = range_y + 5

        # check if we're overlapping with anyone and move off
        # no need to check for zombies as we've already teleported them away

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
                delta_x = -delta_x * move_limit/d
                delta_y = -delta_y * move_limit/d

        # If we're not overlapping anyone, check up on the zombies and see if we should chase one
        if not overlapping:
            all_z = zombie.Zombie.get_all_present_instances()
            if all_z:
                nearest = min(
                    # make pairs of (person, distance from self to person)
                    [ (z, self.distances_to(z) ) for z in all_z ]
                    ,
                    # and sort by distance
                    key=(lambda x: x[1][0])
                    )

                (near_z, near_d) = nearest

                (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
                max_d = ((x_max - x_min) ** 2 + (y_max - y_min) ** 2) ** 0.5

                # if there's a zombie nearby, chase it down
                if near_d[0] <= (max_d/2):
                    (d, delta_x, delta_y, d_edge_edge) = self.distances_to(near_z)

                    if agentsim.debug.get(64):
                        print("nearest zombie to {} is {}, dx {} dy {}".format(
                            self.get_name(), near_z.get_name(), delta_x, delta_y, d_edge_edge))

                    d_edge_edge = round(d_edge_edge, 3)

                    if self.get_move_limit() > d_edge_edge:
                        # if the distance between my edge and the target's edge is smaller than
                        # the move limit, need to reduce delta_x and delta_y so we get as close
                        # to edge as possible

                        new_d = d_edge_edge - (self.get_touching_threshold() + near_z.get_touching_threshold())/2

                        delta_x = delta_x * new_d/d
                        delta_y = delta_y * new_d/d
                else:
                    # No zombies nearby, so move to the middle to defend from zombies teleported to corner
                    x_mid = (x_min + x_max)/2
                    y_mid = (y_min + y_max)/2

                    delta_x = x_mid - self.get_xpos()
                    delta_y = y_mid - self.get_ypos()

                # and change happiness proportional to distance
                (w,h) = agentsim.gui.get_canvas_size()
                diag = (w*w + h*h) ** .5
                delta_h = min( d/diag, .05)
                if agentsim.debug.get(64):
                    print("d", d, "diag", diag, "dh", delta_h)

                self.set_happiness(delta_h + self.get_happiness())

        # alert the normals to huddle in random corner
        # Defenders are all going to teleport zombies to the other corner
        for n in normal.Normal.get_all_present_instances():
            (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()

            if Defender._normal_corner is None:
                # using a dictionary here for logic switching
                # because an if/then construct would have been long
                # and contained redundancies

                dict = {
                        0: (x_min, y_min),
                        1: (x_max, y_min),
                        2: (x_max, y_max),
                        3: (x_min, y_max)
                }

                i = random.randint(0, 3)

                Defender._normal_corner = dict[i]
                Defender._zombie_corner = dict[(i+2) % 4]

            corner = Defender._normal_corner
            n.zombie_alert(corner[0], corner[1])

        return (delta_x, delta_y)

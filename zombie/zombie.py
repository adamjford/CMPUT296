import random
import agentsim
from person import Person
from moveenhanced import MoveEnhanced

# co-dependent imports
import normal
import defender

class Zombie(MoveEnhanced):

    def __init__(self, **keywords):
        MoveEnhanced.__init__(self, **keywords)
        self.set_happiness(1)

        if agentsim.debug.get(2):
            print("Zombie", self._name)

    def get_author(self):
        return "Adam Ford"

    def compute_next_move(self):
        delta_x = 0
        delta_y = 0
        overlapping = False

        # check if we're overlapping with anyone and move off
        # no need to check for normals as we'll just eat them instead >:)

        defenders = defender.Defender.get_all_present_instances()
        zombies = Zombie.get_all_present_instances()

        non_normals = defenders + zombies

        if len(non_normals) > 1:
            nearest = min(
                # make pairs of (person, distance from self to person)
                [ (p, self.distances_to(p) ) for p in non_normals if p.get_id() != self.get_id()]
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
            # find nearest normal if there is one and chase them!
            all_n = normal.Normal.get_all_present_instances()
            if all_n:
                nearest = min(
                    # make pairs of (person, distance from self to person)
                    [ (n, self.distances_to(n) ) for n in all_n ]
                    ,
                    # and sort by distance
                    key=(lambda x: x[1][0])
                    )

                (near_n, near_d) = nearest

                # move towards nearest normal
                (d, delta_x, delta_y, d_edge_edge) = near_d

                if agentsim.debug.get(64):
                    print("nearest normal to {} is {}, dx {} dy {}".format(
                        self.get_name(), near_n.get_name(), delta_x, delta_y, d_edge_edge))

                d_edge_edge = round(d_edge_edge, 3)

                if self.get_move_limit() > d_edge_edge:
                    # if the distance between my edge and the target's edge is smaller than
                    # the move limit, need to reduce delta_x and delta_y so we get as close
                    # to edge as possible

                    new_d = d_edge_edge - self.get_touching_threshold()

                    delta_x = delta_x * new_d/d
                    delta_y = delta_y * new_d/d

                # and change happiness proportional to distance
                (w,h) = agentsim.gui.get_canvas_size()
                diag = (w*w + h*h) ** .5
                delta_h = min( d/diag, .05)
                if agentsim.debug.get(64):
                    print("d", d, "diag", diag, "dh", delta_h)

                self.set_happiness(delta_h + self.get_happiness())

        return (delta_x, delta_y)

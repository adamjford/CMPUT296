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
        delta_y = 0

        # find nearest normal if there is one!
        all_n = normal.Normal.get_all_present_instances()
        if all_n:
            nearest = min(
                # make pairs of (person, distance from self to person)
                [ (n, self.distances_to(n)[0] ) for n in all_n ]
                ,
                # and sort by distance
                key=(lambda x: x[1])
                )

            (near_n, near_d) = nearest

            # move towards nearest normal
            (d, delta_x, delta_y, d_edge_edge) = self.distances_to(near_n)

            if agentsim.debug.get(64):
                print("nearest normal to {} is {}, dx {} dy {}".format(
                    self.get_name(), near_n.get_name(), delta_x, delta_y, d_edge_edge))

            # and change happiness proportional to distance
            (w,h) = agentsim.gui.get_canvas_size()
            diag = (w*w + h*h) ** .5
            delta_h = min( d/diag, .05)
            if agentsim.debug.get(64):
                print("d", d, "diag", diag, "dh", delta_h)

            self.set_happiness(delta_h + self.get_happiness())

        return (delta_x, delta_y)

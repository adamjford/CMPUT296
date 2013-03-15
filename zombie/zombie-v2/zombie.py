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
        return "Your names go here"

    def compute_next_move(self):
        if agentsim.debug.get(128):
            pass

        normals = normal.Normal.get_all_instances()

        if not normals:
            pass

        # find nearest normal
        nearest = min(
            # make pairs of (person, distance from self to person)
            [ (n, self.distances_to(n)[0] ) for n in normals if n.is_present() ]
            ,
            # and sort by distance
            key=(lambda x: x[1])
            )

        (target, near_d) = nearest

        (d, delta_x, delta_y, d_e_e) = self.distances_to(target)

        delta_d = (delta_x * delta_x + delta_y * delta_y) ** 0.5

        if delta_d > self.get_move_limit():
            delta_x = delta_x * self._move_limit / delta_d
            delta_y = delta_y * self._move_limit / delta_d

        too_close = self.is_near_after_move(target, delta_x, delta_y)

        while too_close and not (delta_x == 0 and delta_y == 0):
            delta_x = delta_x/2
            delta_y = delta_y/2

            too_close = self.is_near_after_move(target, delta_x, delta_y)

        if agentsim.debug.get(128):
            print("nearest normal to {} is {}, dx {} dy {}".format(
                self.get_name(), target.get_name(), delta_x, delta_y))

        return (delta_x, delta_y)

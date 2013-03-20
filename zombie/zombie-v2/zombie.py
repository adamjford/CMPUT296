import random
import agentsim
from person import Person
from moveenhanced import MoveEnhanced

# co-dependent imports
import normal
import defender

class Zombie(MoveEnhanced):

    def __init__(self, **keywords):
        super().__init__(**keywords)
        self.set_happiness(1)

        if agentsim.debug.get(2):
            print("Zombie", self._name)

    def get_author(self):
        return "Adam Ford"

    def compute_next_move(self):
        if agentsim.debug.get(128):
            pass

        normals = normal.Normal.get_all_present_instances()

        if not normals:
            # No normals left so nothing left to do
            return (0, 0)

        # find nearest normal
        nearest = min(
            # make pairs of (person, distance from self to person)
            [ (n, self.distances_to(n)) for n in normals ]
            ,
            # and sort by distance
            key=(lambda x: x[1][0])
            )

        (target, near_d) = nearest

        (d, delta_x, delta_y, d_edge_edge) = near_d

        # TODO: Figure out a way to get chaser to get right up to edge of target
        if d_edge_edge < self.get_move_limit():
            t = self.get_touching_threshold()
            ratio = (d_edge_edge - t)/ d
            delta_x = delta_x * ratio
            delta_y = delta_y * ratio

        if agentsim.debug.get(128):
            print("nearest normal to {} is {}, dx {} dy {}".format(
                self.get_name(), target.get_name(), delta_x, delta_y))

        return (delta_x, delta_y)

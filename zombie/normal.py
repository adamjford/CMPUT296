import random
import agentsim
from person import Person
from moveenhanced import MoveEnhanced
import callername
import re

# co-dependent imports
import zombie
import defender

class Normal(MoveEnhanced):

    def __init__(self, **keywords):

        MoveEnhanced.__init__(self, **keywords)

        # this records the information from the most recent
        # zombie alert move.  When compute_next_move() is called, 
        # this information can be processed.

        self._zombie_alert_args = None

        if agentsim.debug.get(2):
            print("Normal", self._name)

        self.set_happiness(1 - 2 * random.random())
        self.set_size(random.uniform(self.get_min_size(), self.get_max_size()))

    def get_author(self):
        return "Adam Ford"

    def compute_next_move(self):
        overlapping = False

        # check if we're overlapping with anyone and move off
        everyone = Person.get_all_present_instances()

        if len(everyone) > 1:
            nearest = min(
                # make pairs of (person, distance from self to person)
                [ (p, self.distances_to(p) ) for p in everyone if p.get_id() != self.get_id()]
                ,
                # and sort by edge-to-edge distance
                key=(lambda x: x[1][3])
                )

            (d, delta_x, delta_y, d_edge_edge) = nearest[1]

            if d > 0 and d_edge_edge < 0:
                # Means we're overlapping with the nearest person
                # Let's move directly away from them and hope they'll
                # do the same
                overlapping = True

                # move in exactly the opposite direction of person
                # with which we're overlapping but move maximum
                # distance allowed
                # We'll still be stuck if move_limit isn't far enough
                # to fix overlap
                move_limit = self.get_move_limit()
                delta_x = -delta_x * (move_limit/d)
                delta_y = -delta_y * (move_limit/d)

        # if we have a pending zombie alert, act on that if we're not overlapping
        if not overlapping and self._zombie_alert_args is not None:
            (x, y) = self._zombie_alert_args
            delta_x = x - self.get_xpos()
            delta_y = y - self.get_ypos()
            # clear the alert
            self._zombie_alert_args = None

        return (delta_x, delta_y)

    def zombie_alert(self, x_dest, y_dest):
        # ignore any request not from a defender!
        caller_name = callername.caller_name()

        if not re.search(r"\.Defender\.", caller_name):
            raise Exception("zombie alert on {} called by non-Defender {}".format(self.get_name(), caller_name))

        if agentsim.debug.get(32):
            print("zombie_alert to ({}, {})".format( self.get_name(), x_dest, y_dest))

        # remember where the alert told us to go so that we can use this
        # information when we compute the next move
        self._zombie_alert_args = (x_dest, y_dest)

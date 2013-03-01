from digraph import Digraph
from least_cost_path import least_cost_path
from testcompare import tcompare
import math

class Server:
    def __init__(self):
        # contents: { vertex_id: ( lat, long ) }
        self.vertex_locations = {}
        # contents: { ( v1, v2 ): name }
        self.edges = {}
        self.graph = Digraph()

    def cost_distance(self, e):
        """
        cost_distance returns the straight-line distance between the two
        vertices at the endpoints of the edge e.

        >>> s = Server()
        >>> s.vertex_locations[275965046] = (53.473513,-113.5199716)
        >>> s.vertex_locations[283173961] = (53.4590515,-113.4263165)
        >>> tcompare(94765, int(s.cost_distance((275965046, 283173961)) * 1000000))
        True
        """
        v1 = self.vertex_locations[e[0]]
        v2 = self.vertex_locations[e[1]]

        return euclidean_distance(v1, v2)

    def closet_vertex(self, lat, long):
        """
        Returns the id of the closest vertex to the specified lat and long
        >>> s = Server()
        >>> s.vertex_locations[275965046] = (53.473513,-113.5199716)
        >>> s.vertex_locations[283173961] = (53.4590515,-113.4263165)
        """

def euclidean_distance(coords1, coords2):
    """
    Returns the Euclidean (straight-line) distance between two coordinates

    >>> tcompare(0, euclidean_distance((0,0), (0,0)))
    True
    >>> tcompare(math.sqrt(2), euclidean_distance((0,0), (1,1)))
    True
    >>> tcompare(math.sqrt(2), euclidean_distance((1,1), (0,0)))
    True
    >>> tcompare(2 * math.sqrt(2), euclidean_distance((-1,-1), (1,1)))
    True
    >>> tcompare(2 * math.sqrt(2), euclidean_distance((1,1), (-1,-1)))
    True
    >>> tcompare(25 * math.sqrt(2), euclidean_distance((-50,-50), (-75, -75)))
    True
    >>> tcompare(25 * math.sqrt(2), euclidean_distance((-75, -75), (-50, -50)))
    True
    >>> tcompare(50 * math.sqrt(13), euclidean_distance((-50, 75), (50, -75)))
    True
    """
    return math.sqrt(math.pow(coords2[0] - coords1[0], 2) + math.pow(coords2[1] - coords1[1], 2))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
if __name__ == "__main__":
    graph = Digraph()

    for line in open('edmonton-roads-2.0.1.txt', 'r'):
        split_line = line.rstrip().split(',')
        line_type = split_line[0]

        if line_type == 'V':
            v = split_line[1]
            graph.add_vertex(v)
            vertices[v] = (split_line[2], split_line[3])
        if line_type == 'E':
            t = (split_line[1], split_line[2])
            graph.add_edge(t)
            edges[t] = split_line[3]

    foo = raw_input()
    (lat1, long1, lat2, long2) = foo.rstrip().split(' ')
"""

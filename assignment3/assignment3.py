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

    def add_vertex(vertex_id, lat, long):
        """
        Adds a vertex and its location to the graph.

        >>> s = Server()
        """

        pass

def cost_distance(e):
    """
    cost_distance returns the straight-line distance between the two
    vertices at the endpoints of the edge e.

    >>> vertices = {}
    >>> vertices[275965046] = (53.473513,-113.5199716)
    >>> vertices[283173961] = (53.4590515,-113.4263165)
    >>> tcompare(0.094765, cost_distance((275965046, 283173961)))
    True

    """
    v1 = vertices[e[0]]
    v2 = vertices[e[1]]

    pass
    #return math.sqrt(math.pow(v2[0] - v1[0], 2) + Math.pow(v2[1] - v1[1], 2)

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

    for line in open('edmonton-roads-digraph.txt', 'r'):
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

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

    def import_file(self, filename):
        """
        Builds the graph and associated information from specified text file.
        """

        print('Importing {}...'.format(filename))
        scale = 100000
        count = 0
        for line in open(filename, 'r'):
            count += 1
            split_line = line.rstrip().split(',')
            line_type = split_line[0]

            if line_type == 'V':
                v = split_line[1]
                self.graph.add_vertex(v)
                self.vertex_locations[v] = (float(split_line[2]) * scale, float(split_line[3]) * scale)
            if line_type == 'E':
                t = (split_line[1], split_line[2])
                self.graph.add_edge(t)
                self.edges[t] = split_line[3]

        print('{} lines processed. Ready for input.'.format(count))

    def cost_distance(self, e):
        """
        cost_distance returns the straight-line distance between the two
        vertices at the endpoints of the edge e.

        >>> s = Server()
        >>> s.vertex_locations[29577354] = (400,-400)
        >>> s.vertex_locations[29770958] = (500,-500)
        >>> tcompare(100 * math.sqrt(2), s.cost_distance((29577354, 29770958)))
        True
        """
        #print('cost_distance: e = {}'.format(e))
        v1 = self.vertex_locations[e[0]]
        v2 = self.vertex_locations[e[1]]
        #print('cost_distance: v1 = {}; v2 = {}'.format(v1, v2))

        return euclidean_distance(v1, v2)

    def closest_vertex(self, lat, long):
        """
        Returns the id of the closest vertex to the specified lat and long
        >>> s = Server()
        >>> s.vertex_locations[29577354] = (5343099.6,-11349133.1)
        >>> s.vertex_locations[29770958] = (5357142.9,-11362729.9)
        >>> s.closest_vertex(5343099,-11349133)
        29577354
        """
        coords = (lat, long)
        closest = min(self.vertex_locations.items(), key=lambda x: euclidean_distance(coords, x[1]))
        return closest[0]

    def find_shortest_path(self, lat1, long1, lat2, long2):
        v1 = s.closest_vertex(lat1, long1)
        v2 = s.closest_vertex(lat2, long2)

        #print('Closest vertices: {} and {}'.format(v1, v2))

        vertex_path = least_cost_path(self.graph, v1, v2, self.cost_distance)
        print('vertex_path: {}'.format(vertex_path))
        path = []

        if vertex_path is not None:
            for v in vertex_path:
                path.append(self.vertex_locations[v])

        return path

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

"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""

if __name__ == "__main__":
    s = Server()
    s.import_file('edmonton-roads-2.0.1.txt')

    while True:
        args = raw_input()

        (lat1, long1, lat2, long2) = args.rstrip().split(' ')

        #print('Finding path between {} and {}...'.format((lat1, long1), (lat2, long2)))

        path = s.find_shortest_path(int(lat1), int(long1), int(lat2), int(long2))

        print(len(path))

        for c in path:
            print('{} {}'.format(c[0], c[1]))

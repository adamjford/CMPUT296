from digraph import Digraph
from least_cost_path import least_cost_path
import Math

# contents: { vertex_id: ( lat, long ) }
vertices = {}
# contents: { ( v1, v2 ): name }
edges = {}

def cost_distance(e):
    """
    cost_distance returns the straight-line distance between the two
    vertices at the endpoints of the edge e.
    >>> cost_distance(
    """
    v1 = vertices[e[0]]
    v2 = vertices[e[1]]

    pass
    #return Math.sqrt(Math.pow(v2[0] - v1[0], 2) + Math.pow(v2[1] - v1[1], 2)

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
    

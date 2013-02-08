"""
Graph module for undirected graphs.
"""

import random
import display

class DiGraph:
    """
    Directed graph.

    The vertices must be comparable and immutable.

    The edge (1, 2) is NOT the same as the edge (2, 1).
    """

    def __init__(self):
        self._adjsets = {}

    def __repr__(self):
        return "DiGraph({})".format(self._adjsets)

    def add_vertex(self, v):
        """
        >>> G = DiGraph()
        >>> G.add_vertex(1)
        >>> G
        DiGraph({1: set([])})
        """
        if v not in self._adjsets:
            self._adjsets[v] = set()

    def add_edge(self, e):
        """
        Adds an edge to graph.  If vertices in the edge do not exist, it adds them.

        >>> G = DiGraph()
        >>> G.add_vertex(1)
        >>> G.add_vertex(2)
        >>> G.add_edge((1, 2))
        >>> G.add_edge((2, 1))
        >>> G.add_edge((1, 3))
        >>> G.num_edges()
        3
        >>> G.num_vertices()
        3
        """
        # Adds the vertices (in case they don't already exist)
        for v in e:
            self.add_vertex(v)

        # Add the edge
        self._adjsets[e[0]].add(e[1])

    def edges(self):
        """
        Returns the set of edges in the graph as ordered tuples.
        >>> G = DiGraph()
        >>> G.add_vertex(1)
        >>> G.add_vertex(2)
        >>> G.add_edge((1, 3))
        >>> G.add_edge((2, 1))
        >>> G.add_edge((1, 2))
        >>> G.edges()
        set([(1, 2), (1, 3), (2, 1)])
        >>> G.add_vertex(4)
        >>> G.edges()
        set([(1, 2), (1, 3), (2, 1)])
        """
        edges = set()

        for key, values in self._adjsets.iteritems():
            for v in values:
                edges.add((key, v))

        return set(sorted(edges))

    def draw(self, filename, attr = {}):
        """
        Draws the graph into a dot file.

        Unimplemented.
        """
        display.write_dot_desc((self._adjsets.keys(), self.edges()), filename, attr)

    def num_edges(self):
        m = 0
        for v in self._adjsets:
            m += len(self._adjsets[v])
        return m

    def num_vertices(self):
        """
        Returns the number of vertices in the graph.
        """
        return len(self._adjsets)

    def adj_to(self, v):
        """
        Returns all vertices directly accessible from v.

        >>> G = DiGraph()
        >>> for v in [1, 2, 3]: G.add_vertex(v)
        >>> G.add_edge((1, 2))
        >>> G.add_edge((2, 1))
        >>> G.add_edge((1, 3))
        >>> G.adj_to(1) == { 2, 3 }
        True
        >>> G.adj_to(2) == { 1 }
        True
        >>> G.adj_to(3) == { 1 }
        False
        """
        return self._adjsets[v]

def random_graph(n, m):
    """
    Make a random Graph with n vertices and m edges.

    >>> G = random_graph(10, 5)
    >>> G.num_edges()
    5
    >>> G.num_vertices()
    10
    >>> G = random_graph(1, 1)
    Traceback (most recent call last):
        ...
    ValueError: For 1 vertices, you want 1 edges, but can only have a maximum of 0
    """
    G = DiGraph()
    for v in range(n):
        G.add_vertex(v)

    max_num_edges = n * (n-1)
    if m > max_num_edges:
        raise ValueError("For {} vertices, you want {} edges, but can only have a maximum of {}".format(n, m, max_num_edges))

    while G.num_edges() < m:
        G.add_edge(random.sample(range(n), 2))

    return G

def spanning_tree(G, start):
    """
    n vertices
    m edges
    """
    visited = set()
    todo = [ (start, None) ]

    T = DiGraph()

    while todo:
        (cur, e) = todo.pop(0)

        if cur in visited: continue

        visited.add(cur)
        if e: T.add_edge(e)

        for n in G.adj_to(cur):
            if n not in visited:
                todo.append((n, (cur, n)))

    return T

def compress(walk):
    """
    Remove cycles from a walk to create a path.

    >>> compress([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> compress([1, 3, 0, 1, 6, 4, 8, 6, 2])
    [1, 6, 2]
    """

    lasttime = {}

    for (i,v) in enumerate(walk):
        lasttime[v] = i

    rv = []
    i = 0
    while (i < len(walk)):
        rv.append(walk[i])
        i = lasttime[walk[i]]+1

    return rv

if __name__ == "__main__":
    import doctest
    doctest.testmod()

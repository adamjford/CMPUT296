"""
Graph example
G = (V, E)
V is a set
E is a set of edges, each edge is an unordered pair
(x, y), x != y
"""

import random
# from random import sample
# from random import *

class Graph:
    """
    Undirected graph.

    The vertices must be comparable.

    The edge (1, 2) is the same as the edge (2, 1).
    """
    
    def __init__(self):
        self._vertices = set()
        self._edges = set()

    def __repr__(self):
        return "Graph({}, {})".format(self._vertices, self._edges)

    def add_vertex(self, v):
        """
        >>> G = Graph()
        >>> G.add_vertex(1)
        >>> G
        Graph({1}, set())
        """
        self._vertices.add(int(v))

    def num_edges(self):
        return len(self._edges)

    def num_vertices(self):
        return len(self._vertices)

    def add_edge(self, e):
        """
        >>> G = Graph()
        >>> G.add_vertex(1)
        >>> G.add_vertex(2)
        >>> G.add_edge((1, 2))
        >>> G.add_edge((2, 1))
        >>> G.add_edge((1, 3))
        >>> G.num_edges()
        2
        >>> G.num_vertices()
        3
        """
        for v in e: self._vertices.add(v)
        self._edges.add((min(e), max(e)))

    def adj_to(self, v):
        """
        >>> G = Graph()
        >>> for v in [1, 2, 3]: G.add_vertex(v)
        >>> G.add_edge((1,2))
        >>> G.add_edge((1,3))
        >>> G.adj_to(1) == {2, 3}
        True
        >>> G.adj_to(3) == {1}
        True
        """
        pass

        neighbours = set()

        for (x,y) in self._edges:
            if v == x: neighbours.add(y)
            if v == y: neighbours.add(x)

        return neighbours

def neighbours_of(G, v):
    """
    >>> G = ( {1, 2, 3}, { (1, 2), (1, 3) })
    >>> neighbours_of(G, 1) == { 2, 3 }
    True
    >>> neighbours_of(G, 3) == { 1 }
    True
    """
    (V, E) = G
    neighbours = set()

    for (x,y) in E:
        if v == x: neighbours.add(y)
        if v == y: neighbours.add(x)

    return neighbours

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
    G = Graph()
    for v in range(n): G.add_vertex(v)

    max_num_edges = n * (n-1) // 2
    if m > max_num_edges:
        raise ValueError("For {} vertices, you want {} edges, but can only have a maximum of {}".format(n, m, max_num_edges))

    while G.num_edges() < m:
        G.add_edge(random.sample(range(n), 2))
        
    return G

def remove_loops(path):
    """
    >>> remove_loops([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> remove_loops([1, 2, 6, 2, 3, 2, 6, 4])
    [1, 2, 6, 4]
    >>> remove_loops([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10])
    [1, 10]
    """
    new_path = []

    while len(path) > 0:
        x = path.pop(0)

        if not x in path:
            new_path.append(x)
        else:
            y = None
            while x in path: 
                y = path.pop(0)
            new_path.append(y)

    return new_path

def compress(walk):
    """
    >>> compress([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> compress([1, 2, 6, 2, 3, 2, 6, 4])
    [1, 2, 6, 4]
    >>> compress([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10])
    [1, 10]
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

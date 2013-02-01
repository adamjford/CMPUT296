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

def generate_random_graph(n, m):
    V = set(range(n))
    E = set()
    max_num_edges = n * (n-1) // 2
    if m > max_num_edges:
        raise ValueError("For {} vertices, you want {} edges, but can only have a maximum of {}".format(n, m, max_num_edges))

    while len(E) < m:
        pair = random.sample(V, 2)
        E.add(tuple([min(pair), max(pair)]))
        
    return (V, E)

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

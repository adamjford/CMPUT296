"""
Graph example
G = (V, E)
V is a set
E is a set of edges, each edge is an unordered pair
(x, y), x != y
"""

import random

def neighbours_of(G, v):
    """
    >>> G = ( {1, 2, 3}, { (1,2), (1,3) })
    >>> neighbours_of(G, 1) == {3, 2}
    True
    >>> neighbours_of(G, 3) == {1}
    True
    """
    (V, E) = G
    neighbours = set()
    for (x, y) in E:
        if v == x: neighbours.add(y)
        if v == y: neighbours.add(x)

    return neighbours

"""
G = ( {1, 2, 3}, { (1,2), (1,3) })
(V, E) = G
start = 1
stop = 3

cur = start
while cur != stop:
    #pick a neighour of cur at random
    neighbours = neighbours_of(G, cur)
    cur = random.sample(neighbours, 1)[0]


"""
if __name__ == '__main__':
    import doctest
    doctest.testmod()

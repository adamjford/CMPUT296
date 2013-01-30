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
    >>> neighbours_of(G, 1) 
    {3, 2}
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

n = 20
m = 5

G = generate_random_graph(n, m)
(V, E) = G

print(G)
print("Number of edges is {}, we want {}".format(len(E), m))

start = random.choice(list(V))
stop = random.choice(list(V))

cur = start

print("Starting at {}".format(cur))
if len(neighbours_of(G, cur)) == 0:
    raise Exception("Bad luck, {} has no neighbours".format(cur))

num_steps = 0
max_num_steps = 1000

while cur != stop and num_steps < max_num_steps:
    num_steps += 1

    # pick a neighbour of cur at random
    neighbours = neighbours_of(G, cur)
    # print(neighbours)
    # pick one of the neighbours
    # cur = random.sample(neighbours, 1)[0]
    # or
    cur = random.choice(list(neighbours))
    print("At {}".format(cur))

print("Finished at {}".format(cur))

"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""

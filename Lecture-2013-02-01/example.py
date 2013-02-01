import random
import graph

n = 20
m = 30

G = graph.generate_random_graph(n, m)
(V, E) = G

# print(G)
print("Number of edges is {}, we want {}".format(len(E), m))

start = random.choice(list(V))
stop = random.choice(list(V))

cur = start

print("Starting at {}".format(cur))
if len(graph.neighbours_of(G, cur)) == 0:
    raise Exception("Bad luck, {} has no neighbours".format(cur))

num_steps = 0
max_num_steps = 1000

history = [cur]

while cur != stop and num_steps < max_num_steps:
    num_steps += 1

    # pick a neighbour of cur at random
    neighbours = graph.neighbours_of(G, cur)
    # print(neighbours)
    # pick one of the neighbours
    # cur = random.sample(neighbours, 1)[0]
    # or
    cur = random.choice(list(neighbours))
    history.append(cur)
    print("At {}".format(cur))

print("Finished at {}".format(cur))
print(history)

"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""

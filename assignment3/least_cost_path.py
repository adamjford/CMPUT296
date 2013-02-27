from digraph import Digraph

def least_cost_path(G, start, dest, cost):
    """
    least_cost_path returns a least cost path in the digraph G from vertex
    start to vertex dest, where costs are defined by the cost function.
    cost should be a function that takes a single edge argument and returns
    a real-valued cost.
    if there is no path, then it returns None
    the path from start to start is [start]

    >>> cost = lambda e: 1
    >>> G = Digraph()
    >>> least_cost_path(G, 1, 2, cost) is None
    True
    >>> G = Digraph([(1, 2)])
    >>> path = least_cost_path(G, 1, 1, cost)
    >>> path
    [1]
    >>> path = least_cost_path(G, 1, 2, cost)
    >>> path
    [1, 2]
    >>> G.is_path(path)
    True
    >>> G = Digraph([(1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (3, 6), (6, 7)])
    >>> path = least_cost_path(G, 1, 7, cost)
    >>> path
    [1, 6, 7]
    >>> G = Digraph([(1, 2), (2, 3), (3, 4), (4, 5), (6, 1), (6, 7)])
    >>> path = least_cost_path(G, 1, 7, cost)
    >>> path is None
    True
    """

    todo = {start:0}
    visited = set()
    parent = {}
    dest_found = False

    while todo and not dest_found:
        (cur, c) = min(todo.items(), key=lambda x: x[1])
        del todo[cur]
        visited.add(cur)
        if cur == dest:
            dest_found = True

        try:
            for n in G.adj_to(cur):
                if n in visited: continue
                if (n not in todo) or todo[n] > c + cost((c,n)):
                    todo[n] = c + cost((c,n))
                    parent[n] = cur
        except KeyError:
            pass

    if not dest_found: return None

    path = [dest]

    while path[0] != start:
        path.insert(0, parent[path[0]])

    return path

if __name__ == "__main__":
    import doctest
    doctest.testmod()

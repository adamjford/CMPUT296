from digraph import Digraph
from collections import OrderedDict

def least_cost_path(G, start, dest, cost):
    """
    todo = {start:0}
    visited = set()
    parent = {}
    while todo and (dest not in visited):
      (cur, c) = todo.pop_smallest()
      visited.add(cur)
      for n in neighbors of cur:
        if n in visited: continue
        if (n not in todo) or todo[n] > c + cost((c,n)):
          todo[n] = c + cost((c,n))
          parent[n] = cur
    Extract path to dest

    >>> cost = lambda e: 1
    >>> G = Digraph()
    >>> least_cost_path(G, 1, 2, cost)
    []
    >>> G = Digraph([(1, 2)])
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
    >>> path
    []
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
            break

    path = []

    if dest_found:
        path.append(dest)
        while path[0] != start:
            foo = parent[path[0]]
            path.insert(0, foo)

    return path

if __name__ == "__main__":
    import doctest
    doctest.testmod()

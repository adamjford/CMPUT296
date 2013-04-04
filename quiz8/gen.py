def mystery(s):
    """
    Returns a generator which generates the unique elements
    in s if they're comparable, in the order in which they
    first appeared.

    Asymptotic running time: O(n^2)

    >>> list(mystery([]))
    []
    >>> list(mystery([1,2,3]))
    [1, 2, 3]
    >>> list(mystery([1,4,2,4,3,7,2,4]))
    [1, 4, 2, 3, 7]
    >>> g = mystery(['a', 'a', 'b'])
    >>> next(g)
    'a'
    >>> next(g)
    'b'
    >>> next(g)
    Traceback (most recent call last):
    ...
    StopIteration
    """

    es = set()
    for e in s:
        if e not in es:
            yield e
            es.add(e)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

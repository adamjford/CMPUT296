def mystery(s):
    """
    WRITE YOUR DOCSTRING HERE.
    """
    
    es = set()
    for e in s:
        if e not in es:
            yield e
            es.add(e)

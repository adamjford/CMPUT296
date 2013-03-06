"""
How to make an == test useful on failure
Source: Dr Hoover, discussion forums
"""

def tcompare(expect, got):
    """
    A compare function that uses the lazy vaulation of or to return True
    or an error string.

    >>> tcompare(1, 1)
    True
    >>> tcompare(1, 2)
    "Compare failed, expected '1' got '2'"
    """
    return ( expect == got or 
        "Compare failed, expected '{}' got '{}'".format(expect, got) )

if __name__ == "__main__":
    import doctest
    doctest.testmod()


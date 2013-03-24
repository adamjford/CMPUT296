def find_largest(l):
    """
    >>> find_largest([1,2,3,4])
    4
    """
    return max(l)

def find_kth_largest(l, k):
    """
    Finds the kth largest thing in a list.

    >>> find_kth_largest([1,2,3,4,5], 2)
    4
    >>> find_kth_largest([2,1,5,4,3], 5)
    1
    """
    return sorted(l)[-k]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

import random

def find_largest(l):
    """
    Finds the largest element of a list.

    >>> find_largest([1,2,3,4])
    4
    """
    # OPTION 1
    return max(l)

    # OPTION 2
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    return largest

def partition(l, pivot, key=lambda x: x):
    """
    Splits the list into three sublists: one with elements less
    than pivot, one with elements equal to pivot, and one with
    elements greater than pivot.

    >>> partition([3, 5, 2, 5, 6, 1, 8], 5)
    ([3, 2, 1], [5, 5], [6, 8])
    """

    key_pivot = key(pivot)

    lt = [ i for i in l if key(i) < key_pivot ]
    eq = [ i for i in l if key(i) == key_pivot]
    gt = [ i for i in l if key(i) > key_pivot ]

    return (lt, eq, gt)

def select_kth(l, k):
    """
    Finds the kth element in the a sorted version of l.

    >>> select_kth([1,2,3,4,5], 3)
    4
    """
    return sorted(l)[k]

def select_kth_fast(l, k, key=lambda x: x):
    """
    Finds the kth element in the a sorted version of l.

    >>> select_kth_fast([1,2,3,4,5], 3)
    4
    >>> select_kth_fast(['hello', 'a', 'jim', 'longer line'], 2, key=lambda x: len(x))
    'hello'
    """
    (lt, eq, gt) = partition(l, random.choice(l), key=key)
    if k < len(lt):
        return select_kth_fast(lt, k, key=key)
    elif k < len(lt) + len(eq):
        return eq[0]
    else:
        return select_kth_fast(gt, k - len(lt) - len(eq), key=key)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    

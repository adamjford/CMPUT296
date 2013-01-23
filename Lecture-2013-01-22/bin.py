
def tobin(x):
    """
    Convert integer to binary representation
    Precondition: x >= 0

    Examples:

    >>> tobin(6) 
    [1, 1, 0]

    >>> tobin(0)
    [0]

    
    """
    if x <= 0: return [0]
    b = []
    while x:
        b.append(x % 2)
        x = x // 2

    b.reverse()
    return b

def toint(b):
    """
    Convert binary representation to integer
    Precondition: entries in list b are 0 and 1

    >>> toint([1, 1, 0]) 
    6

    >>> toint([0, 1, 1, 0])
    6

    >>> toint([0])
    0

    >>> toint([])
    0

    # unexpected good behaviour on a string!
    >>> toint("101")
    5

    Lists do not need to contain the same type of data in each position
    >>> toint([1, "0", 1, "1"])
    11

    """

    result = 0

    for digit in b:
        result = result*2 + int(digit)
    return result


# to run tests do:
# python3 -m doctest -v bin.py 
if __name__ == "__main__":
    import doctest
    doctest.testmod()

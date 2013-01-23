def todigits(x, base):
    """
    Convert x into a list of digits in given base
    
    Examples:
    
    >>> todigits(10, 10)
    [1, 0]

    >>> todigits(1, 10)
    [1]

    >>> todigits(0, 10)
    [0]

    >>> todigits(8, 2)
    [1, 0, 0, 0]

    >>> todigits(10, 2)
    [1, 0, 1, 0]

    >>> todigits(10, 16)
    [10]

    >>> todigits(16, 16)
    [1, 0]

    >>> todigits(16, 16)
    [1, 0]

    >>> todigits(6, 1)
    [1, 1, 1, 1, 1, 1]

    """

    if x <= 0: return [0]
    if base <= 0: return [0]
    b = []
    if base == 1:
        while x:
            b.append(1)
            x = x - 1
    else:
        while x:
            b.append(x % base)
            x = x // base
        b.reverse()

    return b

def tonum(digits, base):
    """
    Convert list of digits in given base to number

    >>> tonum([1, 0], 10)
    10

    >>> tonum([1], 10)
    1

    >>> tonum([0], 10)
    0

    >>> tonum([1, 0, 0, 0], 2)
    8

    >>> tonum([1, 0, 1, 0], 2)
    10

    >>> tonum([10], 16)
    10

    >>> tonum([1, 0], 16)
    16

    >>> tonum([1, 1, 1, 1, 1, 1], 1)
    6

    >>> tonum([1, 2], 2)
    Traceback (most recent call last):
    ...
    Exception: Invalid digit for base 2: 2

    >>> tonum([1, 0], 1)
    Traceback (most recent call last):
    ...
    Exception: Invalid digit for base 1: 0

    >>> tonum([1, 2], 1)
    Traceback (most recent call last):
    ...
    Exception: Invalid digit for base 1: 2

    """

    result = 0

    for digit in digits:
        if (base == 1 and digit != 1) or (base != 1 and digit >= base):
          raise Exception("Invalid digit for base " + str(base) + ": " + str(digit))
        result = result*base + int(digit)
    return result

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


def tobin(x):
    """
    Convert integer to binary representation

    tobin(6) is [1, 1, 0]
    tobin(0) is [0]
    Precondition: x >= 0
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

    toint([1, 1, 0]) is 6
    toint([0, 1, 1, 0]) is 6
    toint([0]) is 0
    toint([]) is 0
    """

    result = 0

    for digit in b:
        result = result*2 + int(digit)
    return result





if __name__ == "__main__":
    import doctest
    doctest.testmod()

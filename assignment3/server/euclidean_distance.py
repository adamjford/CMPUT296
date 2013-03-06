from testcompare import tcompare
import math

def euclidean_distance(coords1, coords2):
    """
    Returns the Euclidean (straight-line) distance between two coordinates

    >>> tcompare(0, euclidean_distance((0,0), (0,0)))
    True
    >>> tcompare(math.sqrt(2), euclidean_distance((0,0), (1,1)))
    True
    >>> tcompare(math.sqrt(2), euclidean_distance((1,1), (0,0)))
    True
    >>> tcompare(2 * math.sqrt(2), euclidean_distance((-1,-1), (1,1)))
    True
    >>> tcompare(2 * math.sqrt(2), euclidean_distance((1,1), (-1,-1)))
    True
    >>> tcompare(25 * math.sqrt(2), euclidean_distance((-50,-50), (-75, -75)))
    True
    >>> tcompare(25 * math.sqrt(2), euclidean_distance((-75, -75), (-50, -50)))
    True
    >>> tcompare(50 * math.sqrt(13), euclidean_distance((-50, 75), (50, -75)))
    True
    """
    return math.sqrt(math.pow(coords2[0] - coords1[0], 2) + math.pow(coords2[1] - coords1[1], 2))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

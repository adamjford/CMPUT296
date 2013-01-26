# Note: This code uses the Python style guide:
#       http://www.python.org/dev/peps/pep-0008/

class Box:

    """
    Box class.

    A Box is a rectangular region described by the positions of its top
    left corner and bottom right corner
        xl, yt, xr, yb
    resulting in 4 coordiate points:
        (xl, yt)    (xr, yt)
        (xl, yb)    (xr, yb)

    Note they are in graphics display orientation, that is (xl,yt) is the top
    left corner, and (xr,yb) is down and to the right.  Thus the specifications
    of the box satisfy the constraints:

        Constraints: xl <= xr, yt <= yb

    In addition to the constructor, 

        b = Box(xl, yt, xr, yb)

    there are these methods for a Box b:

        b.moveBy(dx, dy) - move the (x, y), position of the box b to
            new position (x+dx, y+dy)

        b.contains(x, y) - check if point (x, y) is inside the box b

        b.collidesWith(b1) - check if a box b is touching or overlapping 
            another box b1
        
        b.unionWith(b1) - take a box b and another box b1 and return a new 
            box that is the smallest box that contains both boxes

        b.intersectWith(b1) - take a box b and another box b1 and return a 
            new box that is the intersection of the two boxes.  If the boxes 
            do not overlap, return None.

    NOTE: intersectWith is an optional bonus method.


        >>> b = Box(10, 15, 30, 45)
        
        >>> b.contains(11, 20)
        True

        >>> b.contains(5, 30)
        False

        >>> b.contains(10, 15)
        True

        >>> b.contains(30, 15)
        True

        >>> b.contains(10, 45)
        True

        >>> b.contains(30, 45)
        True

        >>> b.collidesWith(b)
        True

        >>> b1 = Box(11, 10, 20, 20)
        >>> b.collidesWith(b1)
        True
        >>> b1.collidesWith(b)
        True

        >>> b2 = Box(5, 10, 10, 15)
        >>> b2.collidesWith(b)
        True
        >>> b.collidesWith(b2)
        True

        >>> b3 = Box(100, 105, 10, 25)
        >>> b3.collidesWith(b1)
        False
        >>> b1.collidesWith(b3)
        False

        >>> u1 = b.unionWith(b2)
        >>> u1.xl == 5 and u1.yt == 10 and u1.xr == 30 and u1.yb == 45
        True

        >>> bi1 = b2.intersectWith(b) 
        >>> bi1 is None
        True

        >>> bi2 = b.intersectWith(b2)
        >>> bi2 is None
        True

        >>> bi3 = b.intersectWith(b1)
        >>> bi1.xl == 11 and bi1.yt == 15 and bi1.xr == 20 and bi1.yb == 20
        True

        >>> b1.moveBy(2, 3)
        >>> b1.xl == 13 and b1.yt == 13 and b1.xr == 22 and b1.yb == 23
        True

    """

    def __init__(self, xl, yt, xr, yb):
        pass

    def moveBy(self, dx, dy):
        pass
    

# to run tests do:
# python3 box.py -v
if __name__ == "__main__":
    import doctest
    doctest.testmod()

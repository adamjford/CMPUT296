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


        b = Box(xl, yt, xr, yb)
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

        >>> b.moveBy(5, 10)
        >>> [b.xl, b.yt, b.xr, b.yb]
        [15, 25, 35, 55]

        >>> b.moveBy(0, 0)
        >>> [b.xl, b.yt, b.xr, b.yb]
        [15, 25, 35, 55]

        >>> b.contains(11, 20)
        False

        >>> b.moveBy(1, 0)
        >>> [b.xl, b.yt, b.xr, b.yb]
        [16, 25, 36, 55]

        >>> b.moveBy(0, 2)
        >>> [b.xl, b.yt, b.xr, b.yb]
        [16, 27, 36, 57]

        >>> b.collidesWith(b)
        True

        >>> b.moveBy(-4, -4)
        >>> [b.xl, b.yt, b.xr, b.yb]
        [12, 23, 32, 53]

        >>> b = Box(10, 15, 30, 45)
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

        >>> b4 = Box(31, 15, 46, 45)
        >>> b.collidesWith(b4)
        False
        >>> b4.collidesWith(b)
        False

        >>> u1 = b.unionWith(b2)
        >>> [u1.xl, u1.yt, u1.xr, u1.yb]
        [5, 10, 30, 45]

        >>> bi1 = b2.intersectWith(b) 
        >>> [bi1.xl, bi1.yt, bi1.xr, bi1.yb]
        [10, 15, 10, 15]

        >>> bi2 = b.intersectWith(b2)
        >>> [bi1.xl, bi1.yt, bi1.xr, bi1.yb]
        [10, 15, 10, 15]

        >>> bi3 = b.intersectWith(b1)
        >>> [bi3.xl, bi3.yt, bi3.xr, bi3.yb]
        [11, 15, 20, 20]

        >>> b1.moveBy(2, 3)
        >>> [b1.xl, b1.yt, b1.xr, b1.yb]
        [13, 13, 22, 23]

        >>> bx = Box(0, 0, 4, 4)
        >>> by = Box(3, 1, 5, 3)
        >>> bxy = bx.intersectWith(by)
        >>> [bxy.xl, bxy.yt, bxy.xr, bxy.yb]
        [3, 1, 4, 3]

        >>> bx = Box(0, 2, 2, 4)
        >>> by = Box(1, 0, 4, 3)
        >>> bxy = bx.intersectWith(by)
        >>> [bxy.xl, bxy.yt, bxy.xr, bxy.yb]
        [1, 2, 2, 3]

        >>> bx = Box(1, 1, 1, 1)
        >>> by = Box(1, 1, 1, 1)
        >>> bxy = bx.intersectWith(by)
        >>> [bxy.xl, bxy.yt, bxy.xr, bxy.yb]
        [1, 1, 1, 1]

        >>> bx = Box(1, 1, 1, 1)
        >>> by = Box(2, 2, 2, 2)
        >>> bxy = bx.intersectWith(by)
        >>> bxy is None
        True

        >>> bx = Box(50, 50, 100, 100)
        >>> by= Box(150, 150, 200, 200)
        >>> bxy = bx.intersectWith(by)
        >>> bxy is None
        True
    """

    def __init__(self, xl, yt, xr, yb):
        self.xl = xl
        self.yt = yt
        self.xr = xr
        self.yb = yb

    def moveBy(self, dx, dy):
        self.xl += dx;
        self.xr += dx;
        self.yt += dy;
        self.yb += dy;

    def contains(self, x, y):
        return (x >= self.xl and 
                x <= self.xr and 
                y >= self.yt and 
                y <= self.yb)

    def collidesWith(self, b1):
        return (self.contains(b1.xl, b1.yt) or
                self.contains(b1.xl, b1.yb) or
                self.contains(b1.xr, b1.yt) or
                self.contains(b1.xr, b1.yb) or
                b1.contains(self.xl, self.yt) or
                b1.contains(self.xl, self.yb) or
                b1.contains(self.xr, self.yt) or
                b1.contains(self.xr, self.yb))

    def unionWith(self, b1):
        return Box(min(self.xl, b1.xl), min(self.yt, b1.yt), max(self.xr, b1.xr), max(self.yb, b1.yb))

    def intersectWith(self, b1):
        if not self.collidesWith(b1):
            return None
        return Box(max(self.xl, b1.xl), max(self.yt, b1.yt), min(self.xr, b1.xr), min(self.yb, b1.yb))

# to run tests do:
# python3 box.py -v
if __name__ == "__main__":
    import doctest
    doctest.testmod()

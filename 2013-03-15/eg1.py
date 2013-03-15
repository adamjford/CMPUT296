class Shape:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        """
        Pre: abs(dx) + abs(dy) <= 25
        Post: _x = orig(_x) + dx
              _y = orig(_y) + dy
        """
        print("Shape.move_by", dx, dy, self._x, self._y, end=" ")
        self._x += dx
        self._y += dy
        print(self._x, self._y)

class Circle(Shape):
    def __init__(self, r = None, **keywords):
        super().__init__(**keywords)
        self._r = r

class Rectangle(Shape):
    def __init__(self, l = None, w = None, **keywords):
        super().__init__(**keywords)
        self._l = l
        self._w = w


s = Shape(x=42, y=3)
circ = Circle(x=22, y=33, r=1)
rect = Rectangle(x=44, y=55, l=10, w=20)

s.move_by(1, 2)
circ.move_by(3, 4)
rect.move_by(5, 6)

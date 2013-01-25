import math

class Simple:
  """
  >>> p = Simple()
  >>> p.hyp()
  0.0
  >>> p.inc(3, 4)
  >>> p.hyp()
  5.0
  """

  def __init__(self):
    self.x = 0
    self.y = 0

  def inc(self, dx, dy):
    self.x += dx
    self.y += dy

  def hyp(self):
    return math.sqrt(self.x**2 + self.y**2)

if __name__ == "__main__":
  import doctest
  doctest.testmod()

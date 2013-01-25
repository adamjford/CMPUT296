class Dict:
  """
  Data structure that stores key-value pairs and allow querying based on key.

  >>> d = Dict(5)
  >>> d.len()
  0
  >>> d.insert(42, ["Fred", "B+"])
  >>> d.len()
  1
  >>> d.lookup(42)
  ['Fred', 'B+']
  >>> d.lookup(1)
  Traceback (most recent call last):
  ...
  KeyError: 'key not found'
  >>> d.insert(42, ["Fred", "A+"])
  >>> d.lookup(42)
  ['Fred', 'A+']
  """
  
  def __init__(self, size_hint):
    self.keys = []
    self.values = []

  def len(self):
    """
    Returns the number of items in the dictionary.
    """
    return len(self.keys)

  def insert(self, key, value):
    """
    Inserts key-value pair into the dictionary.
    """
    try:
      self.values[self.keys.index(key)] = value
    except ValueError:
      self.keys.append(key)
      self.values.append(value)

  def lookup(self, key):
    """
    Returns the value associated with key. Or raises KeyError if key is not in the dictionary.
    """
    try:
      return self.values[self.keys.index(key)]
    except ValueError:
      raise KeyError('key not found')

if __name__ == "__main__":
    import doctest
    doctest.testmod()

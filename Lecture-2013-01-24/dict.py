class Dict:
  """
  Data structure that stores key-value pairs and allow querying based on key.
  
  Key must be an integer.

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
    self.buckets = []
    for i in range(size_hint):
      self.buckets.append([ [], [] ])

    self.length = 0

  def _hash(self, key):
    """
    Return the hash index for key.
    >>> d = Dict(5)
    >>> d._hash(3)
    1
    >>> d._hash(-2)
    0
    >>> d._hash(0)
    3
    >>> d._hash(7)
    0
    """
    #return key % len(self.buckets)
    h = 0
    for c in str(key):
      h += ord(c)
    return h % len(self.buckets)

  def len(self):
    """
    Returns the number of items in the dictionary.
    """
    return self.length

  def insert(self, key, value):
    """
    Inserts key-value pair into the dictionary.
    """
    try:
      keys, values = self.buckets[self._hash(key)]
      values[keys.index(key)] = value
    except ValueError:
      keys.append(key)
      values.append(value)
      self.length += 1

  def lookup(self, key):
    """
    Returns the value associated with key. Or raises KeyError if key is not in the dictionary.
    """
    keys, values = self.buckets[self._hash(key)]
    try:
      return values[keys.index(key)]
    except ValueError:
      raise KeyError('key not found')

if __name__ == "__main__":
    import doctest
    doctest.testmod()

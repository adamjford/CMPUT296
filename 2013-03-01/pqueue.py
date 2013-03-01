"""
Priority queue implemented with dictionaries.  Stores a set of keys
and associated priorities.

pop_smallest()
  Removes the key with the smallest priority and return a tuple
  with the key and priority.

update(key, priority)
  If priority is lower than the associated priority of key, then
  change key's priority.  If not, does nothing.

  If key is not in the priority queue, add it.

  Returns True if the priority of key is changed or key is added, otherwise False.

is_empty()
  Returns True if empty, else False

>>> q = PQueue()
>>> q.is_empty()
True
>>> q.update("thing", 5)
True
>>> q.is_empty()
False
>>> q.update("another thing", 2)
True
>>> q.pop_smallest()
('another thing', 2)
>>> q.update("thing", 100)
False
>>> q.update("something else", 110)
True
>>> q.update("something else", 8)
True
>>> "thing" in q
True
>>> "nothing" in q
False
>>> len(q)
2
>>> q.pop_smallest()
('thing', 5)
>>> q.pop_smallest()
('something else', 8)
>>> True if q else False
False
>>> q.is_empty()
True

"""

class PQueue:
    def __init__(self):
        self._q = {}

    def __len__(self):
        return len(self._q)

    def __contains__(self, key):
        return key in self._q

    def pop_smallest(self):
        (key, priority) = min(self._q.items(), key=lambda x: x[1])
        del self._q[key]
        return (key, priority)

    def update(self, key, priority):
        do_update = key not in self._q or priority < self._q[key]

        if do_update:
            self._q[key] = priority

        return do_update

    def is_empty(self):
        return len(self._q) == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
  
  

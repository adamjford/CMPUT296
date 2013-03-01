"""
Priority queue implemented with dictionaries.
Stores a set of keys and associated priorities.

Source: class

pop_smallest()
    Removes the key with the smallest priority and returns a tuple
    with the key and priority.

update(key, priority)
    If priority is lower than the associated priority of key,
    then change key's priority. If not, do nothing.

    If key is not in the priority queue, add it.

    Returns nothing.

is_empty()
    Returns True if empty, else False.

>>> q = PQueue()
>>> q.is_empty()
True
>>> q.update("thing", 5)
>>> q.is_empty()
False
>>> "thing" in q
True
>>> "no in there" in q
False
>>> q.update("another thing", 2)
>>> q.pop_smallest()
('another thing', 2)
>>> q.update("thing", 100)
>>> q.update("something else", 110)
>>> q.update("something else", 8)
>>> len(q)
2
>>> q.pop_smallest()
('thing', 5)
>>> q.pop_smallest()
('something else', 8)
>>> q.is_empty()
True
>>> True if q else False
False
>>> q.pop_smallest() is None
True

Binary heap:
    lchild(i) = 2i+1
    rchild(i) = 2i+2
    parent(i) = (i-1)//2
"""

class PQueue:
    def __init__(self):
        self._q = {}

    def __len__(self):
        return len(self._q)

    def __contains__(self, key):
        return key in self._q

    def pop_smallest(self):
        if self.is_empty(): return None

        s = min(self._q.items(), key=lambda x: x[1])
        del self._q[s[0]]
        return s

    def update(self, key, priority):
        if key not in self._q or priority < self._q[key]:
            self._q[key] = priority

    def is_empty(self):
        return len(self._q) == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()

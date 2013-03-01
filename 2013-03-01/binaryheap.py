"""
Priority queue implemented with a binary heap.  Stores a set of keys
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

def _parent(i):
    return (i-1)//2

def _children(i):
    return ( 2*i + 1, 2*i + 2 )

class PQueue:
    def __init__(self):
        self._heap = []
        self._keyindex = {}

    def __len__(self):
        return len(self._heap)

    def __contains__(self, key):
        return key in self._keyindex

    def _key(self, i):
        return self._heap[i][0]

    def _priority(self, i):
        return self._heap[i][1]

    def _swap(self, i, j):
        (self._heap[i], self._heap[j]) = (self._heap[j], self._heap[i])
        self._keyindex[self._key(i)] = i
        self._keyindex[self._key(j)] = j

    def _heapify_down(self, i):
        children = [ c for c in _children(i) if c < len(self._heap) ]

        if not children: return

        minchild = min(children, key=self._priority)
        if self._priority(i) > self._priority(minchild):
            self._swap(i, minchild)
            self._heapify_down(minchild)

    def _heapify_up(self, i):
        if not i: return
        parent = _parent(i)
        if self._priority(i) < self._priority(parent):
            self._swap(i, parent)
            self._heapify_up(parent)

    def pop_smallest(self):
        self._swap(0, len(self._heap)-1)

        # Remove the smallest from the list
        (key, priority) = self._heap.pop()
        del self._keyindex[key]

        self._heapify_down(0)

        return (key, priority)

    def update(self, key, priority):
        if key in self._keyindex:
            i = self._keyindex[key]

            # Check if this lowers its priority
            if priority > self._priority(i):
                return False

            # Fix the heap
            self._heap[i] = (key, priority)
            self._heapify_up(i)
            return True

        else:
            # Add it to the heap
            self._heap.append((key, priority))

            end = len(self._heap)-1
            self._keyindex[key] = end
            self._heapify_up(end)
            return True

    def is_empty(self):
        return len(self._heap) == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()

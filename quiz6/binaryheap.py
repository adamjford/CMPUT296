def _parent(i):
    return (i-1)//2

def _children(i):
    return [ 2*i + 1, 2*i + 2 ]

class PQueue:
    """
    Priority queue implemented as a binary heap.

    pop_smallest()
        remove the element with the lowest priority and
        return the tuple (element, priority)

    update(key, priority)
        lower the priority of an element;
        if priority is not lower then do nothing
        if key is not in the priority queue, add it
        return True if the priority of key is changed or key is added, otherwise False

    is_empty()
        return True if nothing is in the priority queue, otherwise False

    >>> q = PQueue()
    >>> q.is_empty()
    True
    >>> q.update("thing", 1)
    True
    >>> q.is_empty()
    False
    >>> q.update("another thing", 5)
    True
    >>> q.pop_smallest()
    ('thing', 1)
    >>> q.is_empty()
    False
    >>> q.update("thing", 3)
    True
    >>> q.update("another thing", 1)
    True
    >>> q.update("another thing", 10)
    False
    >>> len(q)
    2
    >>> True if q else False
    True
    >>> "another thing" in q
    True
    >>> "nothing" in q
    False
    >>> q.pop_smallest()
    ('another thing', 1)
    >>> q.pop_smallest()
    ('thing', 3)
    >>> q.is_empty()
    True
    >>> for i in range(20): devnull = q.update(i, i)
    >>> len(q)
    20
    >>> [ q.pop_smallest() for i in range(4) ]
    [(0, 0), (1, 1), (2, 2), (3, 3)]
    """

    def __init__(self):
        self._heap = []
        self._keyindex = {}

    def __len__(self):
        return len(self._heap)

    def __contains__(self, key):
        return key in self._keyindex

    def _priority(self, i):
        return self._heap[i][1]

    def _heapify_down(self, i):
        # find my children
        children = [ c for c in _children(i) if c < len(self._heap) ]
        if not children: return
        
        # find the child with the smallest priority
        minchild = min(children, key = self._priority)

        if self._priority(i) > self._priority(minchild):
            # swap i with its minimum child
            self._swap(i, minchild)
            self._heapify_down(minchild)

    def _heapify_up(self, i):
        # if the root, we're done
        if i == 0: return
        
        # compare i with its parent
        if self._priority(i) < self._priority(_parent(i)):
            self._swap(i, _parent(i))
            self._heapify_up(_parent(i))

    def _swap(self, i, j):
        (self._heap[i], self._heap[j]) = (self._heap[j], self._heap[i])
        self._keyindex[self._heap[i][0]] = i
        self._keyindex[self._heap[j][0]] = j
            
    def pop_smallest(self):
        # swap minimum with the last
        self._swap(0, len(self._heap) - 1)

        # remove minimum
        rv = self._heap.pop()
        del self._keyindex[rv[0]]

        # fix the heap
        self._heapify_down(0)
        return rv

    def update(self, key, priority):
        if key in self._keyindex:
            i = self._keyindex[key]

            # check if the new priority is lower 
            if self._priority(i) < priority:
                return False
            else:
                # update priority and fix the heap
                self._heap[i] = (key, priority)
                self._heapify_up(i)
                return True
        else:
            # add it to the end of the heap and fix the heap
            self._heap.append((key, priority))
            self._keyindex[key] = len(self._heap) - 1
            self._heapify_up(len(self._heap)-1)
            return True
        
    def is_empty(self):
        return len(self._heap) == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()

        

    

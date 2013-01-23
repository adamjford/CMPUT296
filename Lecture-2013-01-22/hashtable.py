"""
Module for a simple hashtable.
"""


class HashTable:
    """
    Hash Table

    >>> ht = HashTable(10)
    >>> ht.len()
    0
    >>> ht.insert(4, 'a')
    >>> ht.lookup(4)
    'a'
    >>> ht.lookup(10)
    >>> ht.len()
    1
    """

    def __init__(self, size):
        self.buckets = []
        self.count = 0
        for i in range(size):
            self.buckets.append([])

    def insert(self, key, value):
        """
        Inserts value with the associated key.
        """
        i = key % len(self.buckets)
        self.buckets[i].append((key, value))
        self.count += 1

    def lookup(self, key):
        """
        Returns the value with the associated key.
        """
        i = key % len(self.buckets)
        for keyvalue in self.buckets[i]:
            if keyvalue[0] == key:
                return keyvalue[1]
        return None

    def len(self):
        """
        Returns the number of values in the hash table.
        """
        return self.count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

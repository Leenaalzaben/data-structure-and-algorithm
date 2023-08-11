class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def has(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self.table:
            for pair in bucket:
                keys.append(pair[0])
        return list(set(keys))  
 
 

def hashmap_left_join(T1: HashTable, T2: HashTable):
        """
        Function to left join two hashmaps.

        Returns:
            Hashtable: Hashtable containing the left join result with keys from table1 and values from both tables.
        """
        htb = HashTable()
        for key in T1.keys():
            value1 = T1.get(key)
            value2 = T2.get(key)
            htb.set(key, [value1, value2])
        return htb
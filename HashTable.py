class HashTable:
    # Initiates the Hash Table with a default size, an empty table, load factor, resize, and used slots to keep track of the available space.
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
        self.load_factor = 0.75
        self.resize = 2
        self.used_slots = 0

    # Sets the inital hash value for the given key.
    def _hash(self, key):
        return hash(key) % self.size
    
    # Sets a secondary hash value that will be used in case of a collision.
    def _hash2(self, key):
        return 1 + hash(key) % (self.size - 2)
    
    # Calculates the current load factor. When the load factor is exceeded, the Hash Table will self-resize. 
    def _load_factor(self):
        return self.used_slots / self.size
    
    # Resizes the Hash Table when the load factor is exceeded, all existing key-value pairs will be given a new hash value.
    def _resize(self, update_size):
        update_table = [[] for _ in range(update_size)]
        
        for pair in self.table:
            for key, val in pair:
                update_index = self._hash(key) % update_size
                update_table[update_index].append((key, val))
        
        self.table = update_table
        self.size = update_size

    # Inserts key-value pairs into the Hash Table while handling collisions with double chaining if they occur.
    def insert(self, key, value):
        hash = self._hash(key)
        hash2 = self._hash2(key)
        index = hash

        pair = [key, value]

        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index][1] = value
                return
            
            index = (index + hash2) % self.size
            
        self.table[index].append(pair)

        self.used_slots += 1
        load_factor = self._load_factor()
        
        if load_factor > self.load_factor:
            update_size = self.size * 2
            self._resize(update_size)

    # Retrieves the value associated with the given key if found in the Hash Table, else return an error message.
    def get(self, key):
        index = self._hash(key)

        for kv_pair in self.table[index]:
            if kv_pair[0] == key:
                return kv_pair[1]
        
        return f'Key {key} was not found.'

    # Removes a given key-value pair if the given key is found in the Hash Table, else returns an error message.
    def remove(self, key):
        index = self._hash(key)
        
        for kv_pair in self.table[index]:
            if kv_pair[0] == key:
                self.table[index].remove(kv_pair)
                self.used_slots -= 1
                return

        return f'Key {key} was not found'

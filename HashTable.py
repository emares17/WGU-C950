class Hashmap:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
        self.load_factor = 0.75
        self.resize = 2
        self.used_slots = 0

    def _hash(self, key):
        return hash(key) % self.size
    
    def _hash2(self, key):
        return 1 + hash(key) % (self.size - 2)
    
    def _load_factor(self):
        return self.used_slots / self.size
    
    def _resize(self, update_size):
        update_table = [[] for _ in range(update_size)]
        
        for pair in self.table:
            for key, val in pair:
                update_index = self._hash(key) % update_size
                update_table[update_index].append((key, val))
        
        self.table = update_table
        self.size = update_size

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

    def get(self, key):
        index = self._hash(key)

        for kv_pair in self.table[index]:
            if kv_pair[0] == key:
                return kv_pair[1]
        
        raise KeyError(f'Key {key} was not found.')

    def remove(self, key):
        index = self._hash(key)
        for kv_pair in self.table[index]:
            if kv_pair[0] == key:
                self.table[index].remove(kv_pair)
                self.used_slots -= 1
                return

        raise KeyError(f'Key {key} was not found')



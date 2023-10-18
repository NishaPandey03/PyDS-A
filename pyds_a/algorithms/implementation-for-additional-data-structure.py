class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_value = self._hash_function(key)
        for pair in self.table[hash_value]:
            if pair[0] == key:
                pair[1] = value  # Update value if key already exists
                return
        self.table[hash_value].append([key, value])

    def get(self, key):
        hash_value = self._hash_function(key)
        for pair in self.table[hash_value]:
            if pair[0] == key:
                return pair[1]  # Return value if key is found
        raise KeyError("Key not found in the hash table")

    def remove(self, key):
        hash_value = self._hash_function(key)
        for i, pair in enumerate(self.table[hash_value]):
            if pair[0] == key:
                del self.table[hash_value][i]  # Remove key-value pair if key is found
                return
        raise KeyError("Key not found in the hash table")

# Example Usage
hash_table = HashTable(size=10)
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
hash_table.insert("city", "Wonderland")

print("Name:", hash_table.get("name"))  # Output: Alice
print("Age:", hash_table.get("age"))    # Output: 30

hash_table.remove("age")
try:
    print("Age:", hash_table.get("age"))  # KeyError: Key not found
except KeyError as e:
    print(e)


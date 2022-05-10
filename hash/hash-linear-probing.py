class HashTable:

    def __init__(self):
        # based on the load factor we may change the size of the underlying data structure (
        # dynamic resizing). Load factor is calculated as n/m where n is the number of items in
        # the array and m is the size of the array/list data structure.
        self.capacity = 5
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def hash_function(self, key):
        hash_sum = 0
        for letter in key:
            hash_sum = hash_sum + ord(letter)  # adding ascii values of each letter
        return hash_sum % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            # If same key exists then update the value
            if self.keys[index] == key:
                self.values[index] = value
                return
            # do linear probing and find the next available slot. Here we do mod so as not to
            # exceed the limit of the array
            index = (index + 1) % self.capacity
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            # Return the value if the key matches
            if self.keys[index] == key:
                return self.values[index]
            # do linear probing same as done for insert
            index = (index + 1) % self.capacity
        # Key not found
        return None


if __name__ == '__main__':
    table = HashTable()
    table.insert('Adam', 23)
    table.insert('John', 45)
    table.insert('David', 41)
    table.insert('David', 41)
    table.insert('David', 43)
    table.insert('Steve', 34)
    table.insert('Walter', 29)
    # Commenting the next insert else it will cause the program to go into infinite loop. Need a
    # way to dynamically resize the hash table which will take O(N) linear time.
    # table.insert('Brian', 49)
    print(f'Davids age: {table.get("David")}')
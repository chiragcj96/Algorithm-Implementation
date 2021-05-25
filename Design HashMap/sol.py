'''
Modulo + Array

As one of the most intuitive implementations, we could adopt the modulo operator as the hash function, since the key value 
is of integer type. In addition, in order to minimize the potential collisions, it is advisable to use a prime number as 
the base of modulo, e.g. 2069.

We organize the storage space as an array where each element is indexed with the output value of the hash function.

In case of collision, where two different keys are mapped to the same address, we use a bucket to hold all the values. 
The bucket is a container that hold all the values that are assigned by the hash function. We could use either a LinkedList
or an Array to implement the bucket data structure.

For each of the methods in hashmap data structure, namely get(), put() and remove(), it all boils down to the method to locate 
the value that is stored in hashmap, given the key.

This localization process can be done in two steps:

- For a given key value, first we apply the hash function to generate a hash key, which corresponds to the address in our main 
storage. With this hash key, we would find the bucket where the value should be stored.
- Now that we found the bucket, we simply iterate through the bucket to check if the desired <key, value> pair does exist.

Time Complexity: for each of the methods, the time complexity is O( K/N ) where N is the number of all possible keys and K
is the number of predefined buckets in the hashmap, which is 2069 in our case.

Space Complexity: O(K+M) where K is the number of predefined buckets in the hashmap and M is the number of unique keys that 
have been inserted into the hashmap.

'''
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
                

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]
        
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)
        
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)
    
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
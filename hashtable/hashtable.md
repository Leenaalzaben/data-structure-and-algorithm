# Challenge Title

## **Code Challenge no.30: Hash Table**

### Author : LeeNa Alzaben 

### Approach & Efficiency

| Function        | Time Complexity                  | Space Complexity      | Description                                                      |
|-----------------|----------------------------------|-----------------------|------------------------------------------------------------------|
| `__hash(self, key)` | O(k)                             | O(1)                  | Calculates the hash code for a given key.                         |
| `set(self, key, value)` | O(1) (Average)<br>O(n) (Worst - with collisions) | O(n) (Average - number of elements)<br>O(n^2) (Worst - with collisions) | Adds a key-value pair to the hashtable.                           |
| `get(self, key)` | O(1) (Average)<br>O(n) (Worst - with collisions) | O(1)                  | Retrieves the value associated with the given key.               |
| `has(self, key)` | O(1) (Average)<br>O(n) (Worst - with collisions) | O(1)                  | Checks if a given key exists in the hashtable.                   |
| `keys(self)`    | O(n)                             | O(n)                  | Returns a list of all unique keys present in the hashtable.      |



### Solution

To run the code, you have to pass an array and a value to be inserted:

- Test code: `pytest tests/test_hashtable.py` inside tests file.

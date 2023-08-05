from functools import reduce
from operator import add

class Node:
  def __init__(self, value):
      self.next=None 
      self.value=value


class LinkedList:
  def __init__(self):
    self.head = None


  def insert (self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node


class HashTable:
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []
    self.repeat=[]
    
  
  def __hash(self,key):
    key=str(key)
    return reduce(add, [ord(str(char)) for char in key]) * 283 % self.__size

    
  def set(self,key,value):
    index = self.__hash(key)
    if self.__buckets[index] is None:
      ll = LinkedList()
      self.__buckets[index] = ll
     
    self.__buckets[index].insert([key,value])
    self.keys.append(key)
    

  def get(self,key):
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      while curr :
        if curr.value[0] == key :
          return curr.value[1]
        curr = curr.next  
    return None  
    

  def has(self, key):
    if self.get(key):
      return True
    return False  

  
class TreeNode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None

class binaryTree:
  def __init__(self):
    self.root=None
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    idx = 1

    while idx < len(values):
        current = queue.pop(0)
        if values[idx] is not None:
            current.left = TreeNode(values[idx])
            queue.append(current.left)
        idx += 1

        if idx < len(values) and values[idx] is not None:
            current.right = TreeNode(values[idx])
            queue.append(current.right)
        idx += 1

    return root


def tree_intersection(tree1, tree2):
    """
    Find common values between two binary trees.

    Args:
        tree1 (TreeNode): The root node of the first binary tree.
        tree2 (TreeNode): The root node of the second binary tree.

    Returns:
        set: A set containing the common values present in both trees.
    """
    def traverse_and_build_map(node, value_map):
        """ 
        To traverse tree1 and build value_map 
        """
        if node is None:
            return
        value_map[node.value] = True
        traverse_and_build_map(node.left, value_map)
        traverse_and_build_map(node.right, value_map)

    def find_common_values(node, value_map, output_list):
        """
        To traverse tree2 and find common values
        """
        if node is None:
            return
        if node.value in value_map:
            output_list.add(node.value)
        find_common_values(node.left, value_map, output_list)
        find_common_values(node.right, value_map, output_list)


    value_map = {}
    traverse_and_build_map(tree1, value_map)
    output_list = set()
    find_common_values(tree2, value_map, output_list)
    return output_list

tree1_values = [5, 2, 7, 1, 3, 6, 8]
tree2_values = [2, 1, 3]

tree1 = build_tree(tree1_values)
tree2 = build_tree(tree2_values)

output_list = tree_intersection(tree1, tree2)
print(output_list)
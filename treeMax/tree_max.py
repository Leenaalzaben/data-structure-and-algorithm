from Hash_table.hash_table import Hashtable
from Trees.Trees import Tree,Node

def tree_intersection(Tree1, Tree2):
    """
    takes two binary trees and returns the intersection values between them.

    arguments: 
        two binary trees

    returns: 
        list of intersection values
    """
    obj = Hashtable()
    data = Tree()
    first_tree = data.in_order(Tree1)
    # print(first_tree)
    for x in first_tree:
        obj.set(x ,x)
    second_tree = data.in_order(Tree2)
    return [x for x in second_tree if obj.has(x)]
# Challenge Title : Trees

The code defines three classes: Node, BinaryTree, and BinarySearchTree,which

- Node class: => Represents a node in a binary tree.
- BinaryTree class: => Represents a binary tree.
- BinarySearchTree class: => (inherits from BinaryTree): => Represents a binary search tree, a specialized form of a binary tree.

## Approach & Efficiency

**Approach:** <br>

- The code uses a recursive approach to implement the binary tree and binary search tree operations.
- Recursive algorithms are well-suited for tree-related operations due to the hierarchical nature of trees.

Time Complexity:

- `pre_order_traversal` + `in_order_traversal`+ `post_order_traversal`: <br>
 O(n) =>  because is linear in the number of nodes.
- `add` + `contains`: <br>
O(log n) on average for balanced trees.

Space Complexity:

- `pre_order_traversal` + `in_order_traversal`+ `post_order_traversal`: <br>
 O(n) => The space usage is proportional to the number of nodes.
- `add` + `contains` :<br>
 O(h) => where h is the height of the tree.
- The height becomes equal to the number of nodes, resulting in O(n) space usage.

## Solution

 Show how to run your code => <br>
 `python3 StackAndQueue/trees.py` <br>
 To apply the test use : <br>
 `pytest tests/test_trees.py`<br>
  [Trees](./trees.py)

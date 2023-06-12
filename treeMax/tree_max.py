class Node:
    
    def __init__(self, value):
        """
         New instance of the Node class.

        value: To be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Represents a binary tree data structure."""

    def __init__(self):
        """Initializes a new instance of the BinaryTree class."""
        self.root = None

    def find_maximum_value(self):
        """
        The maximum value in the binary tree.

        Raises:
            An Error If the tree is empty.

        Returns:
            The maximum value in the binary tree.
        """
        if self.root is None:
            raise ValueError(" Tree is empty")
        return self.traverse(self.root)

    def traverse(self, node):
        """
        Recursively traverses the binary tree to find the maximum value.

        Args:
            node: The current node being traversed.

        Returns:
            The maximum value found in the binary tree.
        """
        if node is None:
            return float('-inf')
        
        max_value = node.value
        left_max = self.traverse(node.left)
        right_max = self.traverse(node.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value


# Binary tree
tree = BinaryTree()
tree.root = Node(2)
tree.root.left = Node(7)
tree.root.right = Node(5)
tree.root.left.left = Node(2)
tree.root.left.right = Node(4)
tree.root.right.left = Node(6)
tree.root.right.right = Node(9)
tree.root.left.right.right = Node(11)
tree.root.left.right.lefy = Node(5)


result = tree.find_maximum_value()
print("Maximum value:", result)

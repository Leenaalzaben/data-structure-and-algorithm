class Node:
    """
    Represents a node in a binary tree.

    Attributes:
        value (any): The value stored in the node.
        left (Node): The left child of the node.
        right (Node): The right child of the node.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Node class.

        Args:
            value (any): The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Represents a binary tree.

    Attributes:
        root (Node): The root node of the tree.
    """

    def __init__(self):
        """
        Initializes a new instance of the BinaryTree class.
        """
        self.root = None

    def pre_order_traversal(self, node, result):
        """
        Performs pre-order traversal on the binary tree.

        Args:
            node (Node): The current node being visited.
            result (list): The list to store the traversal result.

        Returns:
            list: The result of the pre-order traversal.
        """
        if node:
            result.append(node.value)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    def in_order_traversal(self, node, result):
        """
        Performs in-order traversal on the binary tree.

        Args:
            node (Node): The current node being visited.
            result (list): The list to store the traversal result.

        Returns:
            list: The result of the in-order traversal.
        """
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)
        return result

    def post_order_traversal(self, node, result):
        """
        Performs post-order traversal on the binary tree.

        Args:
            node (Node): The current node being visited.
            result (list): The list to store the traversal result.

        Returns:
            list: The result of the post-order traversal.
        """
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.value)
        return result


class BinarySearchTree(BinaryTree):
    """
    Represents a binary search tree, which is a specialized form of a binary tree.

    Inherits from:
        BinaryTree
    """

    def __init__(self):
        """
        Initializes a new instance of the BinarySearchTree class.
        """
        super().__init__()

    def add(self, value):
        """
        Adds a value to the binary search tree.

        Args:
            value (any): The value to be added.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        """
        Recursively adds a value to the binary search tree.

        Args:
            node (Node): The current node being visited.
            value (any): The value to be added.
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def contains(self, value):
         """
        Checks if the binary search tree contains a value.

        Args:
            value (any): The value to search for.

        Returns:
            bool: True if the value is found in the binary search tree, False otherwise.
         """
         return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
         """
        Recursively checks if the binary search tree contains a value.

        Args:
            node (Node): The current node being visited.
            value (any): The value to search for.

        Returns:
            bool: True if the value is found in the binary search tree, False otherwise.
         """
         if node is None:
            return False
         if value == node.value:
            return True
         if value < node.value:
            return self._contains_recursive(node.left, value)
         else:
            return self._contains_recursive(node.right, value)


tree = BinaryTree()
tree.root = Node("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")
tree.root.right.left = Node("F")
tree.root.right.right = Node("G")

pre_order_result = tree.pre_order_traversal(tree.root, [])
print("Pre-order", pre_order_result)

in_order_result = tree.in_order_traversal(tree.root, [])
print("In-order", in_order_result)

post_order_result = tree.post_order_traversal(tree.root, [])
print("Post-order", post_order_result)


# Binary Search Tree testing
bst = BinarySearchTree()
bst.add(4)
bst.add(2)
bst.add(6)
bst.add(1)
bst.add(3)
bst.add(5)
bst.add(7)

print("Contains 2:", bst.contains(2))  
print("Contains 8:", bst.contains(8))  
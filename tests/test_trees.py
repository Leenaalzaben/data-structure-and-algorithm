from StackAndQueue.trees import *


def test_empty_tree():
    tree = BinaryTree()
    assert tree.root is None

def test_tree_single_node():
    tree = BinaryTree()
    tree.root = Node("A")
    assert tree.root.value == "A"
    assert tree.root.left is None
    assert tree.root.right is None

def test_binary_tree_add_nodes():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)
    bst.add(1)
    bst.add(3)
    bst.add(5)
    bst.add(7)

    assert bst.root.value == 4
    assert bst.root.left.value == 2
    assert bst.root.right.value == 6
    assert bst.root.left.left.value == 1
    assert bst.root.left.right.value == 3
    assert bst.root.right.left.value == 5
    assert bst.root.right.right.value == 7

def test_pre_order_traversal():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")

    result = tree.pre_order_traversal(tree.root, [])
    expected = ["A", "B", "D", "E", "C", "F", "G"]
    assert result == expected

def test_in_order_traversal():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")

    result = tree.in_order_traversal(tree.root, [])
    expected = ["D", "B", "E", "A", "F", "C", "G"]
    assert result == expected

def test_post_order_traversal():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")

    result = tree.post_order_traversal(tree.root, [])
    expected = ["D", "E", "B", "F", "G", "C", "A"]
    assert result == expected

def test_contains_existing_value():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)
    bst.add(1)
    bst.add(3)
    bst.add(5)
    bst.add(7)

    assert bst.contains(4) is True
    assert bst.contains(2) is True
    assert bst.contains(6) is True
    assert bst.contains(1) is True
    assert bst.contains(3) is True
    assert bst.contains(5) is True
    assert bst.contains(8) is False
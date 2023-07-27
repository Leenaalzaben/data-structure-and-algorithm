import unittest
from TreeIntersection.treeIntersection import TreeNode, tree_intersection

class TestTreeIntersection(unittest.TestCase):

    def setUp(self):
        # Test Tree 1
        self.tree1 = TreeNode(1)
        self.tree1.left = TreeNode(2)
        self.tree1.right = TreeNode(3)
        self.tree1.left.left = TreeNode(4)
        self.tree1.left.right = TreeNode(5)

        # Test Tree 2
        self.tree2 = TreeNode(1)
        self.tree2.left = TreeNode(3)
        self.tree2.right = TreeNode(6)
        self.tree2.left.left = TreeNode(4)
        self.tree2.left.right = TreeNode(7)

    def test_tree_intersection(self):
        result = tree_intersection(self.tree1, self.tree2)
        self.assertEqual(result, {1, 3, 4})

if __name__ == "__main__":
    unittest.main()
import unittest
from TreeIntersection.treeIntersection import TreeNode, tree_intersection

class TestTreeIntersection(unittest.TestCase):

    def test_tree_intersection(self):
        # Test Case 1
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)
        tree1.left.left = TreeNode(4)
        tree1.left.right = TreeNode(5)

        tree2 = TreeNode(1)
        tree2.left = TreeNode(3)
        tree2.right = TreeNode(6)
        tree2.left.left = TreeNode(4)
        tree2.left.right = TreeNode(7)

        result = tree_intersection(tree1, tree2)
        self.assertEqual(result, {1, 3, 4})

        # Test Case 2
        tree1 = TreeNode(10)
        tree1.left = TreeNode(5)
        tree1.right = TreeNode(30)
        tree1.left.left = TreeNode(1)
        tree1.left.right = TreeNode(7)

        tree2 = TreeNode(20)
        tree2.left = TreeNode(30)
        tree2.right = TreeNode(40)
        tree2.left.right = TreeNode(5)

        result = tree_intersection(tree1, tree2)
        self.assertEqual(result, {5, 30})

        # Add more test cases here...

if __name__ == '__main__':
    unittest.main()

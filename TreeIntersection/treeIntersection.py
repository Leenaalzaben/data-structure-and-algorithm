class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def tree_intersection(tree1, tree2):
    tree1_values = in_order_traversal(tree1)
    tree2_values = in_order_traversal(tree2)
    common_values = set(tree1_values) & set(tree2_values)
    return common_values

def in_order_traversal(node):
    if node is None:
        return []
    return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)



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
print(result)  
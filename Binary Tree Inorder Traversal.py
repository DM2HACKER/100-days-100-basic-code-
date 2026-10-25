# Binary Tree Inorder Traversal
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def inorder_traversal(root):
  res = []
  if root:
    res.extend(inorder_traversal(root.left))
    res.append(root.val)
    res.extend(inorder_traversal(root.right))
  return res


# Build a simple tree: 1 -> left: 2, right: 3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(f"Inorder Traversal: {inorder_traversal(root)}")
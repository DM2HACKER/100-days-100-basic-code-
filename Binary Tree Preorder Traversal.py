# Binary Tree Preorder Traversal
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def preorder_traversal(root):
  res = []
  if root:
    res.append(root.val)
    res.extend(preorder_traversal(root.left))
    res.extend(preorder_traversal(root.right))
  return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(f"Preorder Traversal: {preorder_traversal(root)}")
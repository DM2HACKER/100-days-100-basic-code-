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

# Binary Tree Postorder Traversal
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def postorder_traversal(root):
  res = []
  if root:
    res.extend(postorder_traversal(root.left))
    res.extend(postorder_traversal(root.right))
    res.append(root.val)
  return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(f"Postorder Traversal: {postorder_traversal(root)}")


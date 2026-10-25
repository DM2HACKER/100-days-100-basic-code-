# Binary Search Tree (BST) Node Insertion
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def insert(root, val):
  if root is None:
    return TreeNode(val)
  if val < root.val:
    root.left = insert(root.left, val)
  else:
    root.right = insert(root.right, val)
  return root


root = None
for v in [50, 30, 70, 20, 40]:
  root = insert(root, v)

print(f"BST Root Node: {root.val}")
print(f"Left Child of Root: {root.left.val}")
# Find Minimum Element in a BST
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_min_bst(root):
  curr = root
  while curr and curr.left:
    curr = curr.left
  return curr.val if curr else None


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)

print(f"Minimum value in BST: {find_min_bst(root)}")


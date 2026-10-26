# Check if Two Binary Trees are Identical
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def is_same_tree(p, q):
  if not p and not q:
    return True
  if not p or not q or p.val != q.val:
    return False
  return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


root1 = TreeNode(1)
root1.left = TreeNode(2)

root2 = TreeNode(1)
root2.left = TreeNode(2)

print(f"Are the two trees identical? {is_same_tree(root1, root2)}")

# Find Maximum Element in a BST
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_max_bst(root):
  curr = root
  while curr and curr.right:
    curr = curr.right
  return curr.val if curr else None


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.right.right = TreeNode(90)

print(f"Maximum value in BST: {find_max_bst(root)}")
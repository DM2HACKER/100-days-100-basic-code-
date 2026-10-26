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

# Lowest Common Ancestor of a BST
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def lowest_common_ancestor(root, p, q):
  curr = root
  while curr:
    if p.val < curr.val and q.val < curr.val:
      curr = curr.left
    elif p.val > curr.val and q.val > curr.val:
      curr = curr.right
    else:
      return curr
  return None


root = TreeNode(6, TreeNode(2), TreeNode(8))
lca = lowest_common_ancestor(root, root.left, root.right)
print(f"LCA value: {lca.val}")
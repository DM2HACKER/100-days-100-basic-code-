# Valid Parentheses (Using a Stack)
def is_valid_parentheses(s):
  stack = []
  mapping = {")": "(", "}": "{", "]": "["}
  for char in s:
    if char in mapping:
      top_element = stack.pop() if stack else "#"
      if mapping[char] != top_element:
        return False
    else:
      stack.append(char)
  return not stack


print(f"Is '{{[]}}' valid? {is_valid_parentheses('{[]}')}")

# Merge Two Sorted Lists (Linked Lists)
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def merge_two_lists(l1, l2):
  dummy = ListNode(-1)
  curr = dummy
  while l1 and l2:
    if l1.val < l2.val:
      curr.next = l1
      l1 = l1.next
    else:
      curr.next = l2
      l2 = l2.next
    curr = curr.next
  curr.next = l1 if l1 else l2
  return dummy.next


# Quick test setup
l1 = ListNode(1, ListNode(3))
l2 = ListNode(2, ListNode(4))
merged = merge_two_lists(l1, l2)

# Traverse merged list
curr = merged
print("Merged Linked List:", end=" ")
while curr:
  print(curr.val, end=" -> ")
  curr = curr.next
print("None")


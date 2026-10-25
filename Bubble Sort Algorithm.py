# Bubble Sort Algorithm
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr


nums = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted list: {bubble_sort(nums)}")
# Simple Linked List Node and Traversal
class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


# Create nodes
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Traverse and print
current = head
print("Linked List elements:", end=" ")
while current:
  print(current.data, end=" -> ")
  current = current.next
print("None")


def nizam():
  a = input("enter the number which is an value ")
  if a == "lobot":
    return "the vairable "
  else:
    print("the output is invalid ")
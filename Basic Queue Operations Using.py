# Basic Queue Operations Using
from collections import deque

queue = deque()
queue.append(10)  # Enqueue
queue.append(20)
queue.append(30)
print(f"Dequeued element: {queue.popleft()}")
print(f"Remaining queue: {list(queue)}")

# Linear Search Implementation
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

# Binary Search Implementation
def binary_search(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1


sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"Element found at index: {binary_search(sorted_numbers, 23)}")
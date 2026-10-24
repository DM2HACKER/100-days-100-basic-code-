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


numbers = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Element found at index: {linear_search(numbers, target)}")
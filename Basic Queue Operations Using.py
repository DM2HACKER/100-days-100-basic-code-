# Basic Queue Operations Using
from collections import deque

queue = deque()
queue.append(10)  # Enqueue
queue.append(20)
queue.append(30)
print(f"Dequeued element: {queue.popleft()}")
print(f"Remaining queue: {list(queue)}")
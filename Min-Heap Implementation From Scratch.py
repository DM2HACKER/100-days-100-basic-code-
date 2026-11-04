# Min-Heap Implementation From Scratch
class MinHeap:

  def __init__(self):
    self.heap = []

  def parent(self, i):
    return (i - 1) // 2

  def insert(self, key):
    self.heap.append(key)
    self._heapify_up(len(self.heap) - 1)

  def _heapify_up(self, i):
    p = self.parent(i)
    if i > 0 and self.heap[i] < self.heap[p]:
      self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
      self._heapify_up(p)

  def get_min(self):
    return self.heap[0] if self.heap else None


mh = MinHeap()
for val in [3, 1, 6, 5, 2, 4]:
  mh.insert(val)
print(f"Minimum element in heap: {mh.get_min()}")
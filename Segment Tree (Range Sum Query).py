# Segment Tree (Range Sum Query)
class SegmentTree:

  def __init__(self, arr):
    self.n = len(arr)
    self.tree = [0] * (4 * self.n)
    self._build(arr, 0, 0, self.n - 1)

  def _build(self, arr, node, start, end):
    if start == end:
      self.tree[node] = arr[start]
      return
    mid = (start + end) // 2
    self._build(arr, 2 * node + 1, start, mid)
    self._build(arr, 2 * node + 2, mid + 1, end)
    self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

  def query(self, l, r):
    return self._query(0, 0, self.n - 1, l, r)

  def _query(self, node, start, end, l, r):
    if r < start or end < l:
      return 0
    if l <= start and end <= r:
      return self.tree[node]
    mid = (start + end) // 2
    return self._query(2 * node + 1, start, mid, l, r) + self._query(
        2 * node + 2, mid + 1, end, l, r
    )


st = SegmentTree([1, 3, 5, 7, 9, 11])
print(f"Sum of range [1, 3]: {st.query(1, 3)}")
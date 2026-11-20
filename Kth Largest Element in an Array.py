# Kth Largest Element in an Array
import heapq


def find_kth_largest(nums, k):
  min_heap = []
  for num in nums:
    heapq.heappush(min_heap, num)
    if len(min_heap) > k:
      heapq.heappop(min_heap)
  return min_heap[0]


print(f"2nd largest element: {find_kth_largest([3, 2, 1, 5, 6, 4], 2)}")
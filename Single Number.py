# Single Number
def single_number(nums):
  result = 0
  for num in nums:
    result ^= num
  return result


print(f"Single number: {single_number([4, 1, 2, 1, 2])}")

# Majority Element (Boyer-Moore Voting Algorithm)
def majority_element(nums):
  count = 0
  candidate = None
  for num in nums:
    if count == 0:
      candidate = num
    count += 1 if num == candidate else -1
  return candidate


print(f"Majority element: {majority_element([2, 2, 1, 1, 1, 2, 2])}")

# Intersection of Two Arrays
from collections import Counter


def intersect(nums1, nums2):
  c1 = Counter(nums1)
  res = []
  for num in nums2:
    if c1[num] > 0:
      res.append(num)
      c1[num] -= 1
  return res


print(f"Intersection: {intersect([1, 2, 2, 1], [2, 2])}")
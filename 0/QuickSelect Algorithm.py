# QuickSelect Algorithm
import random


def quick_select(nums, k):
  if not nums:
    return None
  pivot = random.choice(nums)
  left = [x for x in nums if x < pivot]
  mid = [x for x in nums if x == pivot]
  right = [x for x in nums if x > pivot]

  if k <= len(left):
    return quick_select(left, k)
  elif k <= len(left) + len(mid):
    return mid[0]
  else:
    return quick_select(right, k - len(left) - len(mid))


print(f"3rd smallest element: {quick_select([3, 2, 1, 5, 6, 4], 3)}")
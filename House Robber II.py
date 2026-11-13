# House Robber II
def rob(nums):
  if len(nums) == 1:
    return nums[0]

  def rob_linear(arr):
    p1, p2 = 0, 0
    for n in arr:
      p1, p2 = max(p2 + n, p1), p1
    return p1

  return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))


print(f"Max money robbed (circular): {rob([2, 3, 2])}")
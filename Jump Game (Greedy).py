# Jump Game (Greedy)
def can_jump(nums):
  max_reach = 0
  for i, num in enumerate(nums):
    if i > max_reach:
      return False
    max_reach = max(max_reach, i + num)
  return True


print(f"Can reach end: {can_jump([2, 3, 1, 1, 4])}")
# Move Zeroes to the End/
def move_zeroes(nums):
  pos = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[pos], nums[i] = nums[i], nums[pos]
      pos += 1
  return nums


print(f"Moved zeroes: {move_zeroes([0, 1, 0, 3, 12])}")

# Longest Common Prefix
def longest_common_prefix(strs):
  if not strs:
    return ""
  strs.sort()
  first, last = strs[0], strs[-1]
  min_len = min(len(first), len(last))
  for i in range(min_len):
    if first[i] != last[i]:
      return first[:i]
  return first[:min_len]


print(
    f"Longest common prefix: {longest_common_prefix(['flower', 'flow', 'flight'])}"
)
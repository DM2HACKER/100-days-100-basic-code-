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


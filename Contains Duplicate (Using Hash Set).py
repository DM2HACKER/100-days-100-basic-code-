# Contains Duplicate (Using Hash Set)
def contains_duplicate(nums):
  return len(nums) != len(set(nums))


print(f"Contains duplicate in [1, 2, 3, 1]? {contains_duplicate([1, 2, 3, 1])}")


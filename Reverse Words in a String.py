# Reverse Words in a String
def reverse_words(s):
  return " ".join(s.strip().split()[::-1])


print(f"Reversed words: {reverse_words('the sky is blue')}")


# Maximum Subarray Sum (Kadane's Algorithm)
def max_subarray(nums):
  max_current = max_global = nums[0]
  for num in nums[1:]:
    max_current = max(num, max_current + num)
    if max_current > max_global:
      max_global = max_current
  return max_global


print(f"Max subarray sum: {max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")

# Find the Missing Number in an Array (1 to N)
def missing_number(nums, n):
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return expected_sum - actual_sum


print(f"Missing number: {missing_number([1, 2, 4, 5, 6], 6)}")


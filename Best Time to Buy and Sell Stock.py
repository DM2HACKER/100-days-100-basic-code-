# Best Time to Buy and Sell Stock
def max_profit(prices):
  min_price = float("inf")
  max_prof = 0
  for price in prices:
    if price < min_price:
      min_price = price
    elif price - min_price > max_prof:
      max_prof = price - min_price
  return max_prof


print(f"Max profit: {max_profit([7, 1, 5, 3, 6, 4])}")

# Remove Duplicates from Sorted Array
def remove_duplicates(nums):
  if not nums:
    return 0
  i = 0
  for j in range(1, len(nums)):
    if nums[j] != nums[i]:
      i += 1
      nums[i] = nums[j]
  return i + 1


nums = [1, 1, 2]
k = remove_duplicates(nums)
print(f"New length: {k}, Array: {nums[:k]}")

# Rotate Array
def rotate(nums, k):
  k %= len(nums)
  nums[:] = nums[-k:] + nums[:-k]
  return nums


print(f"Rotated array: {rotate([1, 2, 3, 4, 5, 6, 7], 3)}")
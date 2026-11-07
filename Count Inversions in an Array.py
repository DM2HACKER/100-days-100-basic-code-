# Count Inversions in an Array
def count_inversions(arr):
  if len(arr) <= 1:
    return arr, 0
  mid = len(arr) // 2
  left, inv_left = count_inversions(arr[:mid])
  right, inv_right = count_inversions(arr[mid:])
  merged, inv_merge = merge_and_count(left, right)
  return merged, inv_left + inv_right + inv_merge


def merge_and_count(left, right):
  result = []
  i = j = inv_count = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      inv_count += len(left) - i
      j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  return result, inv_count


_, total_inversions = count_inversions([8, 4, 2, 1])
print(f"Total inversions: {total_inversions}")

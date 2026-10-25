# Selection Sort Algorithm
def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr


nums = [64, 25, 12, 22, 11]
print(f"Sorted list: {selection_sort(nums)}")
# Insertion Sort Algorithm
def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr


nums = [12, 11, 13, 5, 6]
print(f"Sorted list: {insertion_sort(nums)}")
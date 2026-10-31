# First Unique Character in a String
from collections import Counter


def first_uniq_char(s):
  count = Counter(s)
  for i, ch in enumerate(s):
    if count[ch] == 1:
      return i
  return -1


print(f"First unique character index: {first_uniq_char('leetcode')}")

# Palindrome Linked List

def contains_duplicate(nums):
  return len(nums) != len(set(nums))


print(f"Contains duplicate in [1, 2, 3, 1]? {contains_duplicate([1, 2, 3, 1])}")
# Valid Palindrome
def is_palindrome(s):
  cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
  return cleaned == cleaned[::-1]


test_str = "A man, a plan, a canal: Panama"
print(f"Is '{test_str}' a palindrome? {is_palindrome(test_str)}")
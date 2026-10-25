# Check Anagrams
s1 = input("Enter first string: ").lower().replace(" ", "")
s2 = input("Enter second string: ").lower().replace(" ", "")
if sorted(s1) == sorted(s2):
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.")
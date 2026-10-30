# Reverse Words in a String
def reverse_words(s):
  return " ".join(s.strip().split()[::-1])


print(f"Reversed words: {reverse_words('the sky is blue')}")



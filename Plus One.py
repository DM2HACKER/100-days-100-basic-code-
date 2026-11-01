# Plus One
def plus_one(digits):
  for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
      digits[i] += 1
      return digits
    digits[i] = 0
  return [1] + digits


print(f"Plus one result: {plus_one([1, 2, 9])}")


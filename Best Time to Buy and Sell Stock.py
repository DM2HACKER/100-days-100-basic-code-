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
# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you se
from typing import List


def find_max_profit(price_list: List[int]):
    max_profit = 0
    for p in range(len(price_list)):
        for q in range(p, len(price_list)):
            if q - p > 0 and q - p > max_profit:
                max_profit = q - p
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(find_max_profit(prices))
print("List index-value are : ")

for i in range(len(prices)):
    #print(i, end=" ")
    #print(prices[i])

# Optimized solution
    def maxProfit(prices):
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit
print("maxProfit:", maxProfit(prices))
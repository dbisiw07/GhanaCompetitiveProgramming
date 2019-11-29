import math
def maxProfit(prices):
    min_price = math.inf # set min price to high value initially
    max_profit = 0  # from example 2 max profit cannot be negative
    for price in prices:
        min_price = min(min_price, price)
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)

    return max_profit
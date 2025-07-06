def maxProfit( prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    min_price = prices[0]
    max_prfit = 0  

    for p in prices:
        min_price = min(min_price, p) # 贪心地更新历史最低买入价格
        max_prfit = max(max_prfit, p-min_price)  # 贪心地更新历史最大收益

    return max_prfit

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
print(maxProfit(prices1))
print(maxProfit(prices2))

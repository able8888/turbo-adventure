t=int(input())
for _ in range(t):
    N=int(input())
    prices=list(map(int,input().split()))

    first_buy = float('inf')
    second_buy = float('inf')
    first_profit = 0
    max_profit = 0
    for price in prices:
        # 更新第一次买入后的最小价格和第一次交易的最大利润
        first_buy = min(first_buy, price)
        first_profit = max(first_profit, price - first_buy)

        # 更新第二次买入后的最小价格（考虑第一次利润）和最大总利润
        second_buy = min(second_buy, price - first_profit)
        max_profit = max(max_profit, price - second_buy)
    print(max_profit)





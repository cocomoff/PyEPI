def buy_and_sell_stock_once(prices):
    min_p, max_p = float("inf"), 0
    for p in prices:
        max_p_day = p - min_p
        max_p = max(max_p, max_p_day)
        min_p = min(min_p, p)
    return max_p


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    ans = buy_and_sell_stock_once(A)
    print(ans)

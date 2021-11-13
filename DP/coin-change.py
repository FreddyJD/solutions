def coinChange(coins, amount: int) -> int:
    dp = [float("Inf") for _ in range(amount + 1)]
    dp[0] = 0

    for coin in range(1, amount + 1):
        for change in coins:
            if coin - change >= 0:
                dp[coin] = min(dp[coin], 1 + dp[coin - change])

    if dp[-1] == float("Inf"):
        return -1

    return dp[-1]

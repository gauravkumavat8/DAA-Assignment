def minCoins(coins, amount):
    # Initialize dp array with a large value (infinity)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # No coins are needed to make amount 0
    
    # Iterate through all amounts from 1 to amount
    for i in range(1, amount + 1):
        # For each coin, check if it can contribute to the current amount
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still infinity, it means we can't make the amount
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]  # Coin denominations
amount = 11        # Target amount
print(f"Minimum number of coins: {minCoins(coins, amount)}")  # Output: 3 (5 + 5 + 1)

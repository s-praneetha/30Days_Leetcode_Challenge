class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 1:
            if coins[0] == amount:
                return 1
            elif coins[0]*amount == amount:
                return 1
            elif coins[0]*2 == amount:
                return 1
            elif coins[0] < amount:
                return 0
        dp = [0]*(amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[-1]
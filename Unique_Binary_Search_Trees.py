class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]
        for i in range(1, n+1):
            n = 0
            for j in range(i):
                n += dp[j]*dp[i-j-1]
            dp.append(n)
        return dp[-1]
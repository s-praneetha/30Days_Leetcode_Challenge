class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 1
        tmp_int = len(dungeon[0])+1
        dp = []
        for i in range(len(dungeon)+1):
            dp.append([10000000000] * tmp_int) # max int
        dp[-1][-2],dp[-2][-1],dp[-1][-1] = 1,1,1
        #print(dp)
        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):
                dp[i][j] = max(1,min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j])
        #print(dp)
        return dp[0][0]
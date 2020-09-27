class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(n+m-2) // math.factorial(n-1) // math.factorial(m-1)
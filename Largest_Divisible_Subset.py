class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums):
            nums=sorted(nums)
            dp=[]
            target=[]
            ans=[]
            for i in range(len(nums)):
                target.append(-1)
            for i in range(len(nums)):
                dp.append(1)
                j=0
                while(j<i):
                    if(nums[i]%nums[j]==0):
                        if(dp[i]<dp[j]+1):
                            dp[i]=dp[j]+1
                            target[i]=j
                    j+=1
            temp=max(dp)
            for i in range(len(dp)):
                if(dp[i]==temp):
                    t=i
                    break
            ans.append(nums[t])
            temp=target[t]
            while(temp!=-1):
                ans.append(nums[temp])
                temp=target[temp]
            return ans
        else:
            return []
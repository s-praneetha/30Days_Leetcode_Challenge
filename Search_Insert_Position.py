class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            i = nums.index(target)
            return i
        else:
            nums.append(target)
            nums = [i for i in sorted(nums)]
            j = nums.index(target)
            return j
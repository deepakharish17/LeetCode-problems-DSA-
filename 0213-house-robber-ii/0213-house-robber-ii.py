class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        def robb(nums):
            prev2,prev1=0,0
            for i in nums:
                curr=max(prev1,prev2+i)
                prev2=prev1
                prev1=curr
            return prev1
        skip1=robb(nums[1:])
        skip2=robb(nums[:-1])
        return max(skip1,skip2)
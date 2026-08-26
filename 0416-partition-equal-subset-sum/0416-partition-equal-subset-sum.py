class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum=sum(nums)
        if totalsum%2 !=0:
            return False
        targetSum=totalsum//2
        dp=[False]*(targetSum+1)
        dp[0]=True
        for num in nums:
            for currSum in range(targetSum,num-1,-1):
                dp[currSum]=dp[currSum] or dp[currSum-num]
        return dp[targetSum]
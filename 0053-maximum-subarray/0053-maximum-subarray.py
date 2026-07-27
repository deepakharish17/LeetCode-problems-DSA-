class Solution(object):
    def maxSubArray(self, nums):
        maxi = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            maxi = max(curr_sum, maxi)
            
        return maxi


        #max= -2,1,2,3,4,4
        #i=1,2,3,4,5,6,7,8
        #curr_sum=-2,1,-2,2,1,3,4,-1,4
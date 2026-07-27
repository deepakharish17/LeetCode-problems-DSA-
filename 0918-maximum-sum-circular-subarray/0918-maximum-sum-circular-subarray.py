class Solution(object):
    def maxSubarraySumCircular(self, nums):
        maxsum=nums[0]
        minsum=nums[0]
        currmaxsum=nums[0]
        currminsum=nums[0]
        totalsum=nums[0]
        for i in range(1,len(nums)):
            currmaxsum=max(currmaxsum+nums[i],nums[i])
            maxsum=max(maxsum,currmaxsum)
            currminsum=min(currminsum+nums[i],nums[i])
            minsum=min(minsum,currminsum)
            totalsum+=nums[i]
        currsum=totalsum-minsum
        if currsum==0:
            return maxsum
        return max(maxsum,currsum)
        
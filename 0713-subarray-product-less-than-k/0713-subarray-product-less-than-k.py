class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left=0
        total=0
        curr=1
        for i in range(len(nums)):
            curr*=nums[i]
            while curr>=k:
                curr=curr//nums[left]
                left+=1
            total+=(i-left+1)
        return total

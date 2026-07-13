class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        n=len(nums)
        ans=0
        count=0
        for right in range(n):
            if nums[right]==0:
                count+=1
                while count >k:
                    if nums[left]==0:
                        count-=1
                    left+=1
            ans=max(ans,right-left+1)
        return ans

        
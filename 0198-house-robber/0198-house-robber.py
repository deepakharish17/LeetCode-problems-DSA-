class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev2,prev1=0,0
        for i in nums:
            curr=max(prev2+i,prev1)
            prev2=prev1
            prev1=curr
        return prev1
        
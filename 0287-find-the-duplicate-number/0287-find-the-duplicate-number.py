class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        freq=[0]*(n+1)
        for x in nums:
            if freq[x]==0:
                freq[x]+=1
            else:
                return x
        return 0
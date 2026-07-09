class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        missing=-1
        freq=[0]*(l+1)
        for i in nums:
            freq[i]+=1
        for i in range(l+1):
            if freq[i]==0:
                missing=i
        return missing
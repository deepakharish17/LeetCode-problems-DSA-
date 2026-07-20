class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set()
        pos=0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[pos]=num
                pos+=1
        return pos
        
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cur=ans=0
        for i in nums:
            if i==1:
                cur+=1
                if cur > ans:
                    ans=cur
            else:
                cur=0
        return ans
    
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cur=ans=0
        for i in nums:
            if i==1:
                cur+=1
                ans=max(cur,ans)
            else:
                cur=0
        return ans
    
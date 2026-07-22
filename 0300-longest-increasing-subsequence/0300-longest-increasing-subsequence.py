class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        temp=[]
        temp.append(nums[0])
        for i in range(1,n):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                pos=self.binarysearch(temp,nums[i])
                temp[pos]=nums[i]
        return len(temp)
    def binarysearch(self,temp,target):
        left,right=0,len(temp)-1
        while left<right:
            mid=(left+right)//2
            if temp[mid] <target:
                left=mid+1
            else:
                right=mid
        return left

        
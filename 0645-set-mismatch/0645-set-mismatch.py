class Solution(object):
    def findErrorNums(self, nums):
        l=len(nums)
        missing=-1
        repeated=-1
        freq=[0]*(l+1)
        for num in nums:
            freq[num]+=1
        for i in range(1,l+1):
            if freq[i]==2:
                repeated=i
            elif freq[i]==0:
                missing=i
            if repeated !=-1 and missing !=-1:
                break
        return[repeated,missing]

class Solution:
    def majorityElement(self, nums):
        # return [num for num, count in Counter(nums).items() if count > len(nums) // 3]

        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        res=[]
        for i in freq:
            if freq[i]>len(nums)//3:
               res.append(i)
        return res
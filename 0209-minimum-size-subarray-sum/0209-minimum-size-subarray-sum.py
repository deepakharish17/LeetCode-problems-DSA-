class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        currsum=0
        maxlen=float('inf')
        for i in range(len(nums)):
            currsum+=nums[i]
            while currsum>=target:
                maxlen=min(maxlen, i-start+1)
                currsum-=nums[start]
                start+=1
        return maxlen if maxlen !=float('inf') else 0
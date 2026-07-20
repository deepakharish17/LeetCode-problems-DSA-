class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        pos=0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[pos]=num
                pos+=1
        return pos
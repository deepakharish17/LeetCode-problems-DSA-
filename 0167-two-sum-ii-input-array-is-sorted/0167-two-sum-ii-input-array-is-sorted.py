class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(numbers):
            res=target-num
            if res in seen:
                return [seen[res]+1,i+1]
            seen[num]=i
        
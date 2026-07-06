class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        curr_max=0
        while left<right:
            curr_max=max(curr_max,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return curr_max
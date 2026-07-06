class Solution(object):
    def maxArea(self, height):
        left =0
        right=len(height)-1
        current_max=0
        while left<=right:
            current_max=max(current_max, (right-left)* min(height[left],height[right]))
            if height[left]< height[right]:
                left+=1
            else:
                right -=1
        return current_max
            
        
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ssum=float('inf')
        for i in range(len(nums)-2):
            left,right= i+1,len(nums)-1
            while left <right:
                curr_sum=nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs (ssum - target):
                    ssum=curr_sum
                elif curr_sum > target:
                    right-=1
                elif curr_sum < target:
                    left+=1
                else:
                    return curr_sum
                
        return ssum
# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         nums.sort()
#         closest_sum = float('inf')
        
#         for i in range(len(nums) - 2):
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 current_sum = nums[i] + nums[left] + nums[right]
#                 if abs(current_sum - target) < abs(closest_sum - target):
#                     closest_sum = current_sum
#                 if current_sum < target:
#                     left += 1
#                 elif current_sum > target:
#                     right -= 1
#                 else:
#                     return current_sum
        
#         return closest_sum
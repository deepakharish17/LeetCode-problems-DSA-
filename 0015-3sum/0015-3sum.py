# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         row=[]
#         for i in range(len(nums)-2):
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
#             left =i+1
#             right =len(nums)-1
#             while left<right:
#                 total=nums[i]+nums[left]+nums[right]
#                 if total==0:
#                     row.append([nums[i],nums[left],nums[right]])
#                     while left<right and nums[left]==nums[left+1]:
#                         left+=1
#                     while left>right and nums[right]==nums[right-1]:
#                         right-=1
#                     left+=1
#                     right-=1
#                 elif total<0:
#                     left+=1
#                 else:
#                     right-=1
#         return row
                    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
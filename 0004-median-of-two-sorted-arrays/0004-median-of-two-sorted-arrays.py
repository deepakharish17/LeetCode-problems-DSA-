class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l=len(nums1)  
        if l%2 !=0:
          b = float(nums1[l//2])
          return(b)
        else:
            c = (nums1[(l//2)-1] + nums1[l//2])/2.0
            return(c)

        
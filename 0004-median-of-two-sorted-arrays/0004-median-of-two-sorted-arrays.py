class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        L=len(nums1)
        if L%2 !=0:
            res=float(nums1[L//2])
        else:
            res=(nums1[(L//2)-1] + nums1[L//2])/2.0
        return res
        
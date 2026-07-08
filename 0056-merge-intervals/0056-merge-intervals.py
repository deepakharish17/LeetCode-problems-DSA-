class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        ans=[]
        n=len(intervals)
        i=0
        while i<n:
            left=intervals[i][0]
            right=intervals[i][1]
            j=i+1
            while j<n and intervals[j][0]<=right:
                right=max(right,intervals[j][1])
                j+=1
            ans.append([left,right])
            i=j
        return ans
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        curr=[]
        self.perform(0,target,candidates,ans,curr)
        return ans
    
    def perform(self,index,target,arr,ans,curr):
        if index==len(arr):
            if target==0:
                ans.append(list(curr))
            return
        if arr[index]<=target:
            curr.append(arr[index])
            self.perform(index,target-arr[index],arr,ans,curr)
            curr.pop()
        self.perform(index+1,target,arr,ans,curr)

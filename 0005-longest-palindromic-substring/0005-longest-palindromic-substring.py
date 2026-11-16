# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         bag=set()
#         left,res=0,0
#         for right,ch in enumerate(s):
#             while ch in bag:
#                 bag.remove(ch)
#                 left+=1
#             bag.add(ch)
#             res=max(res,left-right+1)
#         return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
        return ans

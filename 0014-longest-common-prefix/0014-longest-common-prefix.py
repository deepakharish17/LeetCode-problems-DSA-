class Solution:
    def longestCommonPrefix(self, strs):
        s=""
        str1=strs[0]
        for i in range (len(str1)):
            check=True
            for v in strs:
                if i<len(v):
                    if str1[i]!=v[i]:
                        check=False
                else:
                    check=False
            if check:
                s+=str1[i]
            else:
                break
        return s
                
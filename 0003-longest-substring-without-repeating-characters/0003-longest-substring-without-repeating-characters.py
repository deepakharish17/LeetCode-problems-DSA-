class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastseen={}
        start=0
        maxlen=0
        for i in range(len(s)):
            if s[i] in lastseen and lastseen[s[i]]>=start:
                start=lastseen[s[i]]+1
            lastseen[s[i]]=i
            maxlen=max(maxlen,i-start+1)
        return maxlen
        
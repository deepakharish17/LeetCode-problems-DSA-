class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        group={}

        for w in strs:
            key="".join(sorted(w))
            if key in group:
               group[key].append(w)
            else:
                group[key]=[w]
        return list(group.values())
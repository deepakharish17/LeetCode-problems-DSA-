class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        group=defaultdict(list)

        for w in strs:
            key="".join(sorted(w))
            group[key].append(w)
        return list(group.values())
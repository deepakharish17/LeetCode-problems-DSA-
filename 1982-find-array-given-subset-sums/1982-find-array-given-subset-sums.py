from collections import Counter

class Solution(object):
    def recoverArray(self, n, sums):
        sums.sort()
        res = []
        for _ in range(n):
            d = sums[1] - sums[0]
            freq = Counter(sums)
            left, right = [], []
            for x in sums:
                if freq[x] > 0:
                    left.append(x)
                    right.append(x + d)
                    freq[x] -= 1
                    freq[x + d] -= 1
            if 0 in left:
                res.append(d)
                sums = left
            else:
                res.append(-d)
                sums = right
        return res
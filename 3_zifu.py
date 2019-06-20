class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        maxlen = 0
        curlen = 0
        for i in range(n):
            curlen += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                curlen -= 1

            if curlen > maxlen:
                maxlen = curlen
            lookup.add(s[i])
        return maxlen



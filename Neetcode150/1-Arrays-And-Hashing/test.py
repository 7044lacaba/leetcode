list = [1,2,3,1]
class Solution(object):
    def groupAnagrams(self, strs):
        # Time:
        # Space: 
        # Solution:

        ans = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

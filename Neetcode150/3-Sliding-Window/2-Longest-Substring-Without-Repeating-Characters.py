class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        maxlen = 0

        while r < len(s):
            temp = s[l:r]
            if len(temp) > maxlen:
                maxlen = len(temp)
            if s[r] in temp:
                while True:
                    if s[l] == s[r]:
                        l += 1
                        break
                    else:
                        l += 1
            else: 
                r += 1

class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

str = "abcdcaao"
s = Solution()
print(s.lengthOfLongestSubstring(str))
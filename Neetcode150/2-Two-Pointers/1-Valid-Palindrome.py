class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False            
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        if (
            ord("A") <= ord(c) <= ord("Z") or 
            ord("a") <= ord(c) <= ord("z") or 
            ord("0") <= ord(c) <= ord("9")
        ):
            return True
        else:
            return False
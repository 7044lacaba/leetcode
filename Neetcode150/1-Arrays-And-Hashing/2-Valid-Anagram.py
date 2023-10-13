"""
:type s: str
:type t: str
:rtype: bool
"""

class Solution(object):
    def isAnagram(self, s, t):
        # Time:
        # Space: 
        # Solution: Learn replace


        s_copy = s
        t_copy = t

        for item in t_copy:
            if item in s_copy:
                s_copy = s_copy.replace(item, '', 1)
            else:
                return False
        
        if len(s_copy) != 0:
            return False
        return True 
    

class Solution(object):
    def isAnagram(self, s, t):
        # Time: O(2N)
        # Space: 
        # Solution: Use get and a hash map and get()
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
class Solution(object):
    def isAnagram(self, s, t):
        # Time:
        # Space: 
        # Solution:

        return sorted(s) == sorted(t)
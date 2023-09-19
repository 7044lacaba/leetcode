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

        # You can assume they are the same length since we checked earlier, and use the same 
        for i in range(len(s)):
            countS[s[i]] = countS.get([s[i]], 0) + 1
            countT[t[i]] = countS.get([s[t]], 0) + 1
        
        # This takes into account that they are same size, it also checks by character if the key values are the same
        # If there is non this uses '.get' to fetch the key value (default 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
class Solution(object):
    def isAnagram(self, s, t):
        # Time:
        # Space: 
        # Solution:

        return sorted(s) == sorted(t)
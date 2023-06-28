class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
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
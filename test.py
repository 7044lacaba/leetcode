class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_count = {}
        t_count = {}
        l = 0
        r = 0

        for c in t:
            c.lower()
            t_count[c] = t_count.get(c, 0) + 1
        

        
        return t_count




s = "ADOBECODEBANC" 
t = "ABC"

s = Solution()
print(s.minWindow(s, t))

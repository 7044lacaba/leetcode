class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        s1_count = {}
        s2_count = {}

        copy = [*s1]
        for i in range(len(copy)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
        while True:
            if s1_count == s2_count:
                return True

            if s2[l] in s2_count:
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    del s2_count[s2[l]]
            else:
                del s2_count[s2[l]]
            l += 1
            r += 1
            if not r < len(s2):
                break
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            
        return False



s1 = "adc"
s2 = "dcda"

s = Solution()
print(s.checkInclusion(s1, s2))
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = s1[0]

        for i, c in enumerate(s2):
            if first == c:

                copy = [*s1]
                # remove current from copy
                copy.remove(c)
                if len(copy) == 0:
                    return True


                l = i - 1
                r = i + 1

                if l < 0:
                    left = 1
                else:
                    left = s2[l]
                if r >= len(s2):
                    right = 1
                else:
                    right = s2[r]

                while True:
                    if left not in copy and right not in copy:
                        break
                    if left in copy:
                        copy.remove(left)
                        if len(copy) == 0:
                            return True
                        l -= 1
                        left = s2[l]

                    if right in copy:
                        copy.remove(right)
                        if len(copy) == 0:
                            return True
                        r += 1
                        right = s2[r]

        return False

s1 = "mart"
s2 = "karma"

s = Solution()
print(s.checkInclusion(s1, s2))
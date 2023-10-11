# class Solution(object):
#     def characterReplacement(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         ret = 0 
#         l, r = 0, 1
#         lives = k 
#         counter = 1

#         while r < len(s):
#             if s[l] == s[r]:
#                 r += 1
#                 counter += 1
#                 if counter > ret:
#                     ret = counter
#             else:
#                 if lives > 0:
#                     r += 1
#                     counter += 1
#                     lives -= 1
#                     if counter > ret:
#                         ret = counter
#                 else:
#                     base = s[l]
#                     while True:
#                         l += 1
#                         if s[l] != base:
#                             r = l
#                             counter = 0
#                             lives = k
#                             break
#         return ret

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret = 0 
        l, r = 0, 0
        dic = {}
        most = 0

        while r < len(s):
            dic[s[r]] = dic.get(s[r], 0) + 1
            most_freq = max(dic.values())
            window_size = len(s[l:(r + 1)])
            diff = window_size - most_freq

            if diff <= k:
                current = window_size
                if current > most:
                    most = current 
                r += 1
            else:
                id = s[l]
                dic[id] -= 1
                l += 1
        return most


str = "AABABBA"
k = 1
s = Solution()
print(s.characterReplacement(str, k))
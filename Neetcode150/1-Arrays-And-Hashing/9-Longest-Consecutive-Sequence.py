class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        final = 0 

        for item in nums:
            if (item - 1) not in numSet:
                consec = 0
                while (item + consec) in numSet:
                    consec += 1
                final = max(consec, final)
        return final

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Time: O(N^2)
        # Space: O(N)
        # Solution I came up with
        copy = nums
        for i, item in enumerate(copy):
            copy.pop(i)
            if item in copy:
                return True
        return False
    
        # Time: (nlogn)
        # Space: O(1)
        # Optimized solution

        hashset = set()

        for item in nums:
            if item in hashset:
                return True
            hashset.add(item)
        return False
        
        
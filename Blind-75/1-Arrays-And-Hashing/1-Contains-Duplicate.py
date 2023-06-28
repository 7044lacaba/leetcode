"""
:type nums: List[int]
:rtype: bool
"""


class Solution(object):
    def containsDuplicate(self, nums):
        # Time: O(N^2)
        # Space: O(N)
        # Solution I came up with
        
        copy = nums
        for i, item in enumerate(copy):
            copy.pop(i)
            if item in copy:
                return True
        return False
    
class Solution(object):
    def containsDuplicate(self, nums):
        # Time: (nlogn)
        # Space: O(1)
        # Optimized solution

        hashset = set()

        for item in nums:
            if item in hashset:
                return True
            hashset.add(item)
        return False
        
        
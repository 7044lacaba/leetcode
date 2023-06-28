"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""

class Solution(object):
    def twoSum(self, nums, target):
        # Time: O(N^2)
        # Space: 
        # Solution: 

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution(object):
    def twoSum(self, nums, target):
        # Time: O(N)
        # Space: O(N)
        # Solution: 

        maps = {}
        for i, item in enumerate(nums):
            diff = target - item
            if diff in maps:
                return [maps[diff], i]    
            maps[item] = i
        return
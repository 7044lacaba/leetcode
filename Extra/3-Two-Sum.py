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
        for i, item in enumerate(nums):
            try: 
                if (target - item) in nums[i + 1::]:
                    other_val = nums.index((target - item), (i + 1), len(nums))
                    return[i, other_val]
            except:
                return False

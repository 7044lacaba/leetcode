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

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        for i, item in enumerate(nums):
            try: 
                if (target - item) in nums[i + 1::]:
                    other_val = nums.index((target - item), (i + 1), len(nums))
                    return[i, other_val]
            except:
                return False

class Solution(object):
    def twoSum(self, nums, target):
        # Time: O(N)
        # Space: O(N)
        # Solution: 

        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
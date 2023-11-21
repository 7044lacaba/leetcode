class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        
        length = len(nums)
        mid = int(length / 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            new_list = nums[mid:]
            return self.search(new_list, target) + mid
        elif nums[mid] > target:
            new_list = nums[:mid]
            return self.search(new_list,target)
        









s = Solution()
nums = [-1,0,3,5,9,12]
target = 13
print(s.search(nums, target))
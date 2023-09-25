class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Runtime: O(N^2)

        final = []
        for i, item in enumerate(nums):
            temp = nums.copy()
            temp.pop(i)
            value = 1
            for item in temp:
                value = value * item
            final.append(value)
        return final
    

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Runtim: O(N)
        # Memory: O(N)

        final = []

        value_before = 1
        for i, current in enumerate(nums):
            final.append(value_before * current)
            value_before = value_before * current

        post_side = 1
        for i, current in enumerate(nums[::-1]):

            temp = (i - (len(nums) - 2))
            pre_side_index = abs(i - (len(nums) - 2))
            post_side_index = abs(i - len(nums))
            final_index = abs(i - (len(nums) - 1))
            if i > 0:    
                post_side = post_side * nums[post_side_index]

            if temp > 0:
                pre_side = 1
            else:
                pre_side = final[pre_side_index]
            insert = pre_side * post_side
            final[final_index] = insert

        return final

  
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
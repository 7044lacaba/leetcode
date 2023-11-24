# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         max_list = []
#         l = 0 
#         r = k
#         while r < len(nums) + 1:
#             window = nums[l:r]
#             window.sort()
#             max_list.append(window[k - 1])
#             l += 1
#             r += 1
#         return max_list







class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        l = 0 
        r = k - 1

        stack = []
        final = []

        # prep everything to starting position 
        for temp_r in range(0, k - 1):
            if len(stack) == 0:
                stack.append(nums[temp_r])
            elif nums[r] > stack[-1]:
                stack.pop(-1)
                stack.append(nums[temp_r])
            else:
                stack.append(nums[temp_r])
        
        # loop through rest of nums 
        while r < len(nums):
            
            if nums[r] > stack[-1]:
                stack.pop(-1)
                stack.append(nums[temp_r])
            else:
                stack.append(nums[temp_r])
            
            final.append(stack[0])

            if nums[r] == stack[0]:
                stack.pop(0)




nums = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))








# start window, add  
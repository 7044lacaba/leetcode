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



## Neet solution

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         output = []
#         q = collections.deque()  # index
#         l = r = 0
#         # O(n) O(n)
#         while r < len(nums):
#             # pop smaller values from q
#             while q and nums[q[-1]] < nums[r]:
#                 q.pop()
#             q.append(r)

#             # remove left val from window
#             if l > q[0]:
#                 q.popleft()

#             if (r + 1) >= k:
#                 output.append(nums[q[0]])
#                 l += 1
#             r += 1

#         return output






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
            else:
                while stack and nums[temp_r] > stack[-1]:
                    stack.pop(-1)
                stack.append(nums[temp_r])
        
        # loop through rest of nums 
        while r < len(nums):
            while stack and nums[r] > stack[-1]:
                stack.pop(-1)
            stack.append(nums[r])
            final.append(stack[0])
            if nums[l] == stack[0]:
                stack.pop(0)
            l += 1
            r += 1
        
        return final

# 3, 3, 5, 5, 6, 7


nums = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))








# start window, add  
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_list = []
        l = 0 
        r = k
        while r < len(nums) + 1:
            window = nums[l:r]
            window.sort()
            max_list.append(window[k - 1])
            l += 1
            r += 1
        return max_list


nums = [1,3,-1,-3,5,3,6,7]
k = 3


s = Solution()
print(s.maxSlidingWindow(nums, k))








# start window, add  
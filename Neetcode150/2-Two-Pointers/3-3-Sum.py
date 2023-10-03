class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        final = []

        for i, n in enumerate(nums):
            l = (i + 1)
            r = (len(nums) - 1)
            if l == r:
                break
            opp = 0 - n
            while l != r and l < r:
                sum = nums[l] + nums[r]
                if sum < opp:
                    l += 1
                elif sum > opp:
                    r -= 1
                else:
                    add = [n, nums[l], nums[r]]
                    if add not in final:
                        final.append(add)
                    l += 1
                    r -= 1
        return(final)

# nums = [-1,0,1,2,-1,-4]
# s = Solution()
# print(s.threeSum(nums))
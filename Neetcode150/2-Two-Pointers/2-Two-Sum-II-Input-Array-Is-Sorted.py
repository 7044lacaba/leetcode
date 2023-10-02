class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_1 = 0
        index_2 = 1
        dic = {}
        while index_1 != index_2:
            # Add first into dict
            value = target - numbers[index_1]
            dic[value] = index_1
            # Check item at index 2
            if numbers[index_2] in dic:
                ret = [(dic[numbers[index_2]] + 1), (index_2 +1)]
                return(ret)
            # Increment
            if index_2 + 1 == len(numbers):
                index_1 += 1
            else:
                index_1 += 1
                index_2 += 1

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_l = 0
        index_r = (len(numbers) - 1)
        while index_l != index_r:
            val_l = numbers[index_l]
            val_r = numbers[index_r]
            sum = val_l + val_r
            if sum > target:
                index_r -= 1
            elif sum < target:
                index_l += 1
            else:
                return [(index_l + 1), (index_r + 1)]
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
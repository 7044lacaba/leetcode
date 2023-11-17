class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        nested_list_stack = []
        final = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while nested_list_stack and temp > nested_list_stack[-1][0]:
                temp_diff = i - nested_list_stack[-1][1]
                final[nested_list_stack[-1][1]] = temp_diff
                nested_list_stack.pop()

            nested_list_stack.append([temp, i])
        return final


# you can make variables = to items in a list 
# stackT, stackInd = stack.pop() -> [73, 0]





s = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(s.dailyTemperatures(temperatures))
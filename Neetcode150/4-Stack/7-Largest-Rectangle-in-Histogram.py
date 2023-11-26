# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         maxArea = 0
#         stack = []  # pair: (index, height)

#         for i, h in enumerate(heights):
#             start = i
#             while stack and stack[-1][1] > h:
#                 index, height = stack.pop()
#                 maxArea = max(maxArea, height * (i - index))
#                 start = index
#             stack.append((start, h))

#         for i, h in stack:
#             maxArea = max(maxArea, h * (len(heights) - i))
#         return maxArea








# my solution

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # [index, height]
        stack = []
        most_cells = 0
        for i, num in enumerate(heights):
            current_height_and_index = [i, num]
            while stack and num < stack[-1][1]:
                # pop and calculate 
                top_stack_index = stack[-1][0]
                top_stack_height = stack[-1][1]
                cells = (i - top_stack_index) * top_stack_height
                if cells > most_cells:
                    most_cells = cells
                current_height_and_index[0] = top_stack_index
                stack.pop()
            stack.append(current_height_and_index)
        end = len(heights)
        for pair in stack:
            cells = (end - pair[0]) * pair[1]
            if cells > most_cells:
                most_cells = cells
        return most_cells

heights = [2,4]
s = Solution()
print(s.largestRectangleArea(heights))
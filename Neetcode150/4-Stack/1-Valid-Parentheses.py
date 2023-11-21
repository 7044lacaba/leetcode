# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 == 1:
#             return False
#         stack = []
#         for item in s:
#             if self.opening(item) == True:
#                 stack.append(item)
#             else:
#                 try:
#                     if self.checkPair(item, stack[len(stack) - 1]) == False:
#                         return False
#                     else:
#                         stack.pop(len(stack) - 1)
#                 except:
#                     return False
#         if len(stack) == 0:
#             return True
#         else:
#             return False

#     def opening(self, s: str) -> bool:
#         if s == "(" or s == "[" or s == "{":
#             return True
#         return False

#     def checkPair(self, s_1: str, s_2: str) -> bool:
#         if s_1 == ")":
#             if s_2 == "(":
#                 return True
#             else:
#                 return False
#         elif s_1 == "}":
#             if s_2 == "{":
#                 return True
#             else:
#                 return False
#         elif s_1 == "]":
#             if s_2 == "[":
#                 return True
#             else:
#                 return False
#         else:
#             return False




class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")": "(", "]": "[", "}": "{"}
        stack = []

        for item in s:
            if item in dict:
                if stack and dict[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        
        if len(stack) == 0:
            return True
        else:
            return False        








st = "}{"

s = Solution()
print(s.isValid(st))

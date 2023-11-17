class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for item in tokens:

            try:
                num = int(item)
            except:
                int_1 = stack[-1]
                int_2 = stack[-2]
                stack.pop()
                stack.pop()
                
                if item == "+":
                    stack.append(int_2 + int_1)
                elif item == "-":
                    stack.append(int_2 - int_1)
                elif item == "*":
                    stack.append(int_2 * int_1)
                elif item == "/":

                    stack.append(int(int_2 / int_1))
            else: 
                stack.append(num)
        return(stack[0])
                

        







## interger division always rounds down, we need division that rounds towards 0, - 1.5 -> -2.0


s = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(s.evalRPN(tokens))
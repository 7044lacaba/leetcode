class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        final = []
        sub_list = []

        def helper_function(open_count, close_count):

            if open_count == close_count == n:
                final.append("".join(sub_list))
                return
            

            if open_count < n:
                # can open
                sub_list.append("(")
                helper_function(open_count + 1, close_count)
                sub_list.pop()


            if open_count > close_count:
                # can close
                sub_list.append(")")
                helper_function(open_count, close_count + 1)
                sub_list.pop()


        
        helper_function(0, 0)
        return final




s = Solution()
print(s.generateParenthesis(3))


    ## make sure you write about the join method
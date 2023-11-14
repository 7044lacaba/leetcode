class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """






        
        final = []
        sub_list = []

        open_count = 0
        close_count = 0

        self.helper_function(final, sub_list, open_count, close_count, n)

        print(final)



    def helper_function(self, final, sub_list, open_count, close_count, n):
        

        if open_count == close_count == n:
            ret = ("".join(sub_list))
            return ret



        if open_count > close_count:
            # can close
            copy_1 = sub_list
            copy_1.append(")")
            close_1 = close_count + 1
            open_1 = open_count
            final.append(self.helper_function(copy_1, open_1, close_1, n))



        
        if open_count < n:
            # can open
            copy_2 = sub_list
            copy_2.append("(")
            open_2 = open_count + 1
            close_2 = close_count
            final.append(self.helper_function(copy_2, open_2, close_2, n))





s = Solution()
s.generateParenthesis(3)


    ## make sure you write about the join method
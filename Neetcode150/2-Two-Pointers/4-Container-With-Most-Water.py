class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = 1
        end = len(height) - 1
        ret = 0

        while l != end:
            r = l + 1
            
            while r < len(height):
                val_l = height[l]
                val_r = height[r]
                if val_l < val_r:
                    h = val_l
                else:
                    h = val_r
                w = r - l
                total = w * h
                if total > ret:
                    ret = total
                r += 1
            l += 1
        
        return(ret)



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        l = 0
        r = len(height) - 1

        while l < r and l != r:
            val_l = height[l]
            val_r = height[r]
            if val_l < val_r:
                h = val_l
            else:
                h = val_r
            w = r - l
            total = w * h
            if total > ret:
                ret = total
            if val_l < val_r:
                l += 1
            else:
                r -= 1
        return(ret)
        

# height = [1,8,6,2,5,4,8,3,7]
# s = Solution()
# print(s.maxArea(height))
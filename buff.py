class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_ptr = 0
        r_ptr = 0
        list = []
        second = [0,0]
        water = 0

        while r_ptr < (len(height) - 1):

            if height[r_ptr] >= height[l_ptr]:
                water += self.convert(list, height[l_ptr])
                list = []
                l_ptr = r_ptr
            else:
                list.append(height[r_ptr])
                if height[r_ptr] >= second[0]:
                    second[0] = height[r_ptr]
                    second[1] = r_ptr
            
            #check if at end 
            if r_ptr + 1 == (len(height) - 1):
                







    def convert(self, list, convert_val):
        total_water = 0
        for item in list:
            water = convert_val - item
            total_water += water
        return total_water
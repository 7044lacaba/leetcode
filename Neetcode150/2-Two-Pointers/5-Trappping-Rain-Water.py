class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # find start

        start = 0
        for i, n in enumerate(height):
            if n > height[i + 1]:
                start = i
                break
        
        # keep moving right pointer untill increase/equal is found 

        l_pntr = start
        r_pntr = start
        prev_val = 0

        max = height[l_pntr]

        convert_list = []
        middle = 0 

        while r_pntr < (len(height) - 1):
            
            # move right pointer

            r_pntr += 1

            # check for increase 


            # if next bar increases then move left and calculate the inside 
            if height[r_pntr] >= height[l_pntr]:
                # for item in convert list find the water value and add then up
                # clear convert list 
                pass
                # l_pntr = r_pntr
            else:
                convert_list.append(height[])

# only enter the left pointer value if >=

    def convert(self, list, convert_val):
        total_water = 0
        for item in list:
            water = convert_val - item
            total_water += water
        return total_water
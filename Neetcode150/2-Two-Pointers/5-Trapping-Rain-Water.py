class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_ptr = 0
        r_ptr = 0
        second = [0,0]
        water = 0
        prev_value = 0
        while r_ptr != len(height):
            # check if previous value is 
            # check if valid right wall is found
            if height[r_ptr] >= height[l_ptr]:

                # convert val = the shorter wall
                if height[r_ptr] > height[l_ptr]:
                    convert_val = height[l_ptr]
                elif height[r_ptr] < height[l_ptr]:
                    convert_val = height[r_ptr]
                else:
                    convert_val = height[l_ptr]
                
                # convert sublist into water and add to total
                sublist = height[(l_ptr + 1):r_ptr]
                water += self.convert(sublist, convert_val)

                # update left pointer
                l_ptr = r_ptr

                # reset the second highest
                second = [0,0]
            
            else:
                # check and update second highest
                if height[r_ptr] >= second[0]:
                    second[0] = height[r_ptr]
                    second[1] = r_ptr
            
            # if at end convert any valid values 
            if r_ptr == (len(height) - 1) and l_ptr != r_ptr:
                water += self.convert(height[(l_ptr + 1): second[1]], second[0])
                return water
            
            # update previous value
            prev_value = height[r_ptr]
            r_ptr += 1
        return water

    def convert(self, list, convert_val):
        total_water = 0
        for item in list:
            water = convert_val - item
            if water > 0:
                total_water += water
        return total_water
    

class Solution:
    def trap(self, height):
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


height = [5,4,1,2]
s = Solution()
print(s.trap(height))
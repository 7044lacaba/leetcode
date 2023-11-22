class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pos_and_speed = []
        stack = []

        # for i in range(len(position)):
        #     pos_and_speed.append([position[i], speed[i]])

        print(zip(position, speed))

        for p, s in zip(position, speed):
            pos_and_speed.append([p, s])
        
        print(pos_and_speed)
        print(sorted(pos_and_speed))

        for pair in sorted(pos_and_speed)[::-1]:
            time = (target - pair[0]) / pair[1]
            stack.append(time)


            # you pop the faster value because itll get stuck behind the slower car (remmeber we're iterating in reverse order)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)



# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [(p, s) for p, s in zip(position, speed)]
#         pair.sort(reverse=True)
#         stack = []
#         for p, s in pair:  # Reverse Sorted Order
#             stack.append((target - p) / s)
#             if len(stack) >= 2 and stack[-1] <= stack[-2]:
#                 stack.pop()
#         return len(stack)



# zip to to iterate through two list of same len
# or you can use a hash map and sort by position


target = 10
position = [0,4,2]
speed = [2,1,3]

s = Solution()
print(s.carFleet(target, position, speed))

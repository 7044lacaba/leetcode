class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        count  = 0
        while True:

            for i in range(len(target)):
                position[i] = position[i] + speed[i]






# zip 
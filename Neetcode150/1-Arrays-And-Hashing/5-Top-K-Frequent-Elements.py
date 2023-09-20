class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()

        current = nums[0]
        counter = 0
        dict = {}

        for i, item in enumerate(nums):
            if (i + 1) == len(nums) and item != current:
                dict[current] = counter
                dict[item] = 1
            elif (i + 1) == len(nums):
                dict[current] = counter + 1
            elif current != item:
                dict[current] = counter
                current = item
                counter = 1
            elif current == item:
                counter += 1


        temp = len(dict)
        final = []

        while len(final) != temp:
            current = 0
            most = 0
            for item in dict:
                if dict[item] > most:
                    most = dict[item]
                    current = item
            final.append(current)
            del dict[current]

        return final[:k]



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        list = []
        for i in range(len(nums) + 1):
            sub = []
            list.append(sub)

        for item in nums:
            dict[item] = 1 + dict.get(item, 0)
        for k, v in dict.items():
            list[v].append(k)

        print(dict)
        print(list)
        final = []
        for i in range(len(list) - 1, 0, -1):
            for n in list[i]:
                final.append(item)
                if len(final) == k:
                    return final
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        list_val = [0] * k
        list_key = [0] * k
        
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        
        for item in dict:
            for i, spot, in enumerate(list_val):
                if dict[item] > list_val[i]:
                    list_val[i] = dict[item]
                    list_key[i] = item
                    break
        return list_key
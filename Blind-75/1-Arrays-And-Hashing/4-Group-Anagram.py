"""
:type strs: List[str]
:rtype: List[List[str]]
"""

class Solution(object):

    # Time:
    # Space: 
    # Solution:

    def checker(self, s_1, s_2):
        for item in s_2:
            if item in s_1:
                s_1 = s_1.replace(item, '', 1)
            else:
                return False
        
        if len(s_1) != 0:
            return False
        return True 

    def groupAnagrams(self, strs):
        final_list = []
        for i, s_1 in enumerate(strs):
            if  any(s_1 in sublist for sublist in final_list) == True:
                continue
            sub_list = []
            for j, s_2 in enumerate(strs, i + 1):
                if self.checker(s_1, s_2) == True:
                    sub_list.append(s_2)
            final_list.append(sub_list)
        return final_list


class Solution(object):
    def groupAnagrams(self, strs):
        # Time:
        # Space: 
        # Solution:

        d = {}

        for word in strs:
            key = tuple(sorted[word])
            d[key] = d.get(key, []) + [word]
        
        return d.values()
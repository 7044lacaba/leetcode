"""
:type strs: List[str]
:rtype: List[List[str]]
"""
from collections import defaultdict

class Solution(object):

    # Time:
    # Space: 
    # Solution:
    
    def groupAnagrams(self, strs):
        # Initalize
        copy = strs
        final_list = []

        # Repeat untill no more left in main list
        while len(copy) != 0:

            # Hold current item and remove from main list
            current = copy[0]
            copy.pop(0)

            # Initalize sublist and add current item
            sublist = [current]
            
            # Check if current item is a anagram to anything in our remaining list
            # Loop through subcopy since we are editing the list copy
            subcopy = copy
            for item in subcopy:

                # If anagram then add it to sublist 
                subcopy = copy
                for i, item in enumerate(subcopy):

                    # If anagram then add it to sublist (using checker function)
                    if sorted(current) == sorted(item):
                        sublist.append(item)
                        copy.pop(i)
            
            # Once all same anagrams are added to sublist then append it to the main list
            final_list.append(sublist)

        return final_list


class Solution(object):
    def groupAnagrams(self, strs):
        # Time:
        # Space: 
        # Solution:

        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""


from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Dictionary to store the count of each number in the input list
        count_dict = {}

        # Count occurrences of each number in the input list
        for num in arr:
            count_dict[num] = count_dict.get(num, 0) + 1

        # Check if the number of unique counts is equal to the total number of counts
        if len(set(count_dict.values())) == len(count_dict.values()):
            # If equal, all occurrences are unique, so return True
            return True
        else:
            # If not equal, there are duplicate occurrences, so return False
            return False

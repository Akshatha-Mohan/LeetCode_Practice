'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_nums = [-1] * len(arr)
        max_seen = -1
        for i in range(len(arr)-1, 0, -1):
            if(arr[i] > max_seen):
                max_seen = arr[i]
            max_nums[i-1] = max_seen
            
        return max_nums
            
        
        

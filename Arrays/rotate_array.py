'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr = [0]*len(nums)
        for i in range(len(nums)):
            j = (i+k) % (len(nums))
            arr[j] = nums[i]

        nums[:] = arr
        
        
        

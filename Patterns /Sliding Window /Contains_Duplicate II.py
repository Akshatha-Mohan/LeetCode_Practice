"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k. 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
""" 1) HASHMAP """
        seen = {}
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            # Update the most recent index for this number
            seen[num] = i
        
        return False

""" 2) SLIDING WINDOW """
        window = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False

        

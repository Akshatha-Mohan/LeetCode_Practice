"""
HASHMAP
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious 
subsequence among all its possible subsequences.

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # nums = sorted(nums)
        # left = 0
        # window_length = 0

        # for right in range(len(nums)):
        #     while nums[right] - nums[left] > 1:  # Ensure `diff` is at most 1
        #         left += 1
        #     if nums[right] - nums[left] == 1:  # Valid harmonious subsequence
        #         window_length = max(window_length, right - left + 1)

        # return window_length

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        print(freq)
        
        max_length = 0
        for num in freq:
            # If num+1 exists in the array, we have a harmonious subsequence
            if num + 1 in freq:
                # Length is sum of frequencies of num and num+1
                length = freq[num] + freq[num + 1]
                max_length = max(max_length, length)
        
        return max_length

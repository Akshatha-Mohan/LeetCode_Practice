"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

IDEA: Have prefix and postfix list of products. 1st traverse through input get prefix values 
1) for nums = [1,2,3,4] we traverse from beginning => output = [1, 1, 2, 6]
  suffix getting updated [24,12,4,1], gets carried over in next iteration
2) postfix from end we traverse => [24,12,8,6]
TC: O(N)
Space : O(1)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n

        # Calculate prefix products
        prefix_prod = 1
        for i in range(n):
            output[i] *= prefix_prod
            prefix_prod *= nums[i]

        # Calculate suffix products
        suffix_prod = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix_prod
            suffix_prod *= nums[i]

        return output





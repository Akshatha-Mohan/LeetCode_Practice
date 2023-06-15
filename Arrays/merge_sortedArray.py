'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
'''
IDEA : 2 pointers, reading through nums1 and nums2 -> 1st while checks nums1 and nums2 < or > -> 2nd and 3rd while append remaining elements
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        result = []
        while i < m and j < n:
            if (nums1[i] < nums2[j]):
                #append for non-iterable data type (int)
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < m:
            result.append(nums1[i])
            i += 1
        while j < n:
            result.append(nums2[j])
            j += 1
        nums1[:] = result
        
        
        
        
        
        
        

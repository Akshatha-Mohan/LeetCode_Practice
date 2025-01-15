class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            # Update the most recent index for this number
            seen[num] = i
        
        return False

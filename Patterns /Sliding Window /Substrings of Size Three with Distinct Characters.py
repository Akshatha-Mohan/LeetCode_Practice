"""
A string is good if there are no repeated characters. Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

 
Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
"""


class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3:
            return 0
            
        count = 0
        # We only need to go up to len(s)-2 because we're looking at 3 chars at a time
        for i in range(len(s)-2):
            # Get substring of length 3
            substr = s[i:i+3]
            # If length of set equals 3, all characters are unique
            if len(set(substr)) == 3:
                count += 1
        return count

  

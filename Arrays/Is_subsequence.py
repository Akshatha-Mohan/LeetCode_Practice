"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        match = []
        last = -1
        for i in range(len(s)):
            for j in range(last+1, len(t)):
                if(s[i] == t[j]):
                    match.append(j)
                    last = j
                    break

        sorted_list = sorted(match)
        if(len(match) == len(s)):
                return True
        return False
        """

        LEFT = len(s)
        RIGHT = len(t)
        p_left = p_right = 0
        while(p_left < LEFT and p_right < RIGHT):
            if(s[p_left] == t[p_right]):
                p_left += 1
            p_right += 1

        return p_left == LEFT
      
      
      
      
      

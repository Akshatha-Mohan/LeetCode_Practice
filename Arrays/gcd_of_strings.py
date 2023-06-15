'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
'''
'''
IDEA: TAKE gcd of len(str1) and len(str2) and return str1[:gcd], and make sure that str1 + str2 == str2 + str1
'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        gcd_length = gcd(len(str1), len(str2))
        gcd_str = str1[:gcd_length]
        
        if str1 + str2 == str2 + str1:
            return gcd_str
        else:
            return ""
          
          
          
          

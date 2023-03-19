"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = collections.Counter(s)
        print(freq)
        count_even = 0
        count_odd = 0
        total_length = 0
        #keep a track of even and odd frequencies
        for char, freq in freq.items():
            if freq % 2 == 0:
                count_even += 1
                total_length += freq
            else:
              #odd frequencies - 1 to make it even and then add to final length
                count_odd += freq                
                total_length += freq - 1

        if count_odd > 0:
            total_length = 1 + total_length

        return total_length
      
      """
      s = "abccccdd"
      Stdout Counter({u'c': 4, u'd': 2, u'a': 1, u'b': 1})
      """
      
      
      
      
      
      
        
            

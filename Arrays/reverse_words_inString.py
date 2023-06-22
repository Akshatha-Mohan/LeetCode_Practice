"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
IDEA: parse through the string twice and remove trailing and leading spaces
the  extract each char, and once you encounter a space and word is present appendleft to QUEUE
AND join these using spaces and return queue
TC: O(N)
SC: O(N)

"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s)

        for i in range(len(s)):
            if s[i] == " ":
                start += 1
            elif s[i]!= " ":
                break
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                end -= 1
            elif s[i]!= " ":
                break

        d = collections.deque()
        word = []
        while start < end:
            if s[start] == " " and word:
                #each input char joined as a word
                d.appendleft("".join(word))
                word = []
            elif s[start]!= " ":
                word.append(s[start])
            start += 1
            
        #for the last word
        d.appendleft("".join(word))
        return (" ".join(d))







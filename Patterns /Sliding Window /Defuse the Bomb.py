"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. 
Notice that the numbers wrap around.
"""



class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(code)
        result = [0] * N
        start, end, window_sum = 1,k,0
        
        if k<0:
            start, end = N-abs(k), N-1

        for i in range(start, end+1):
            window_sum += code[i]

        for i in range(len(code)):
            result[i] = window_sum
            window_sum -= code[start % N]
            window_sum += code[(end+1) % N]
            start += 1
            end += 1
        return result




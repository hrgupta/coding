'''Leetcode Top Interview Questions
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
'''Solution
'''Solution
109 / 109 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 13.6 MB
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        carry = 1
        while(n>=0):
            if(digits[n]<9):
                digits[n] += 1
                carry = 0
                break
            else:
                digits[n] = 0
            n-=1
        if(carry==1):
            digits = [1]+digits
        return digits
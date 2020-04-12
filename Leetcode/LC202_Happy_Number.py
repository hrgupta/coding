'''
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
'''Solution
401 / 401 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 13.8 MB
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        nums = []
        while(1):
            s = sum(list(map(lambda x: x*x, map(int, str(num)))))
            if(s==1):
                return True
            if(s in nums):
                return False
            nums.append(s)
            num = s
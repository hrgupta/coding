'''Leetcode 30-day challenge
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
'''Solution
16 / 16 test cases passed.
Status: Accepted
Runtime: 84 ms
Memory Usage: 16.3 MB
'''
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_t = defaultdict(int)
        for i in nums:
            hash_t[i] += 1
        
        for i in hash_t:
            if hash_t[i] == 1:
                return i
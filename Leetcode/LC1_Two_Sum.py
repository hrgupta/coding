"""Leetcode Top Interview Questions
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
"""
Solution:
29 / 29 test cases passed.
Status: Accepted
Runtime: 32 ms
Memory Usage: 14 MB
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in h:
                return [h[n], i]
            h[num] = i
        return []
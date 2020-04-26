"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
"""
Solution:

Runtime: 116 ms, faster than 61.60% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 16.2 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K.

Explanation:

###
"""
class Solution:
    def subarraySum(self, nums, k):
        count, cur, res = {0: 1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res
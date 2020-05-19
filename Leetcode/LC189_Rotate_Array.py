'''Leetcode Top Interview Questions
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''
'''Solution
35 / 35 test cases passed.
Status: Accepted
Runtime: 64 ms
Memory Usage: 15.3 MB
'''
class Solution:
    def reverse(self, nums, start, end):
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0 , n -1)
        self.reverse(nums,0, k-1)
        self.reverse(nums, k, n-1)
        return nums
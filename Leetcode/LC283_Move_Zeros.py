'''Leetcode Top Interview Questions
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
'''Solution
'''Solution
21 / 21 test cases passed.
Status: Accepted
Runtime: 56 ms
Memory Usage: 15.1 MB
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        i=-1
        j=-1
        while(j<n):
            j+=1
            if(nums[j]!=0):
                i+=1
                nums[i] = nums[j]
        print('i',i)
        print('j',j)
        while(i<j):
            i+=1
            nums[i]=0
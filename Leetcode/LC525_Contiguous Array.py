'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''
'''
Solution:
555 / 555 test cases passed.
Status: Accepted
Runtime: 864 ms
Memory Usage: 18.3 MB
'''
from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = defaultdict(int)
        count_map[0] = -1
        count = 0
        maxlen = 0
        for i,n in enumerate(nums):
            count = count + ( 1 if n==1 else -1)
            if(count in count_map):
                maxlen = max(maxlen, i - count_map[count])
            else:
                count_map[count] = i
        return maxlen
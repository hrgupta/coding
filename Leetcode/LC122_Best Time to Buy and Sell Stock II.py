'''Leetcode Top Interview Questions
 Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

'''
'''Solution
200 / 200 test cases passed.
Status: Accepted
Runtime: 64 ms
Memory Usage: 15.1 MB
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i =0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while(i < len(prices) -1):
            while (i < len(prices)-1 and prices[i] >= prices[i+1]):
                i+=1
            valley = prices[i]
            while (i < len(prices)-1 and prices[i] <= prices[i+1]):
                i+=1
            peak =  prices[i]
            maxprofit += peak - valley
        return maxprofit
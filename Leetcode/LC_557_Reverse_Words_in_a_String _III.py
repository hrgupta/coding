'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
'''Solution
30 / 30 test cases passed.
Status: Accepted
Runtime: 64 ms
Memory Usage: 14.4 MB
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        print(words)
        result = []
        for word in words:
            rword = ''.join(reversed(word))
            result.append(rword)
        output = ' '.join(result)
        return output
'''Leetcode Top Interview Questions
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
'''Solution
27 / 27 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 15.4 MB
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(not head or not head.next):
            return head
        reverse = head
        li = head.next
        reverse.next = None
        while(li):
            temp = ListNode()
            temp.val = li.val
            temp.next = reverse
            reverse = temp
            li = li.next
        return reverse
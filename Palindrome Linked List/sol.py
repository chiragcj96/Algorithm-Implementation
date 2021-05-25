# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Here the intuition is to create an Array of all Node values and return if the reverse is equal to itself
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        value = []
        while (head):
            value.append(head.val)
            head = head.next
        return value == value[::-1]
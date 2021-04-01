# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        current = head
        i = 1
        j = 0
        while current:
            print(current.val, i, j)
            if i == m:
                node = current.next
                while j < n and node:
                    node = node.next
                    j += 1
                j = 0
                current.next = node
                current = node
                i = 1
            elif current:
                current = current.next
                i += 1
        return head
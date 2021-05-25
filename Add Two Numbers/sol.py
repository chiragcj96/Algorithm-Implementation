# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
    
#         l1Val, l2Val, output = [], [], []
#         temp = l1
#         l3 = n = ListNode(0)
#         while (temp):
#             l1Val.append(temp.val)
#             temp = temp.next
#         temp = l2
#         while (temp):
#             l2Val.append(temp.val)
#             temp = temp.next
#         print(l1Val, l2Val)
#         carry = 0
#         for i in range(min(len(l1Val), len(l2Val))):
#             # print(i, l1Val[i], l2Val[i])
#             output.append(int((l1Val[i] + l2Val[i] + carry)%10))
#             carry = (l1Val[i] + l2Val[i] + carry)/10
#             # print(output)
#         if len(l1Val)>len(l2Val):
#             larger = l1Val
#         else: 
#             larger = l2Val
#         # print(larger)
#         while i<len(larger)-1:
#             output.append(int((larger[-i-1]+carry)%10))
#             carry = int((larger[-i-1]+carry)/10)
#             print(int((larger[-i-1]+carry)%10), carry)
#             print(output)
#             i+=1
#         if int(carry)>0:
#             output.append(int(carry))
#         for o in output:
#             n.next = ListNode(o)
#             n = n.next
#         return l3.next
        
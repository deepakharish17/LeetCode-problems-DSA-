# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def getDecimalValue(self, head: ListNode | None) -> int:
#         count=1
#         num=0
#         cur = head
#         while cur:
#             cur=cur.next;
#             count*=2
#         count//=2
#         cur=head
#         while cur:
#             num+=cur.val*count
#             count//=2
#             cur=cur.next
#         return num

class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        num = 0
        while head:
            num = num * 2 + head.val  
            head = head.next
        return num


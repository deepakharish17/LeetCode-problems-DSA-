# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        temp=head
        res={}
        while temp is not None:
            if temp in res:
                return True
            res[temp]=1
            temp=temp.next
        return False
#  hasCycle(self, head: Optional[ListNode]) -> bool:
#         fast=head
#         slow=head
#         while fast is not None and fast.next is not None:
#             fast=fast.next.next
#             slow=slow.next
#             if slow==fast:
#                 return True
#         return False
        
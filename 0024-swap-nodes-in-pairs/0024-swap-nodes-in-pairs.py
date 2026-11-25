# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: ListNode | None) -> ListNode | None:
#         curr=head
#         while curr and curr.next:
#             curr.val,curr.next.val = curr.next.val,curr.val
#             curr=curr.next.next
#         return head

class Solution:
    # def swapPairs(self, head: ListNode | None) -> ListNode | None:
    #     dummy = ListNode(0, head)
    #     prev = dummy
    #     while prev.next and prev.next.next:
    #         first = prev.next
    #         second = prev.next.next

    #         first.next = second.next
    #         second.next = first
    #         prev.next = second

    #         prev = first
    #     return dummy.next

    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        new_head = head.next if head and head.next else head
        prev = None
        while head and head.next:
            second = head.next
            head.next = second.next
            second.next = head

            if prev:
                prev.next = second
        
            prev = head
            head = head.next

        return new_head
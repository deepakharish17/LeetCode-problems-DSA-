# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        temp=head
        res={}
        while temp is not None:
            if temp in res:
                return True
            res[temp]=1
            temp=temp.next
        return False

        
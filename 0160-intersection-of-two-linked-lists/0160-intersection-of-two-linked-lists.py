# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # def getdifference(self,headA, headB):
    #     len1,len2=0,0
    #     while headA or headB:
    #         while headA:
    #             len1+=1
    #             headA=headA.next
    #         while headB:
    #             len2+=1
    #             headB=headB.next
    #     return len1-len2
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista = headA
        listb = headB
        while lista != listb:
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA
        return listb
    #     diff = self.getdifference(headA,headB)

    #     if diff < 0:
    #         while diff !=0:
    #             headB=headB.next
    #             diff+=1
    #     else:
    #         while diff!=0:
    #             headA=headA.next
    #             diff-=1
    #     while headA != headB:
    #         headA = headA.next
    #         headB = headB.next
            
    #     return headA


       
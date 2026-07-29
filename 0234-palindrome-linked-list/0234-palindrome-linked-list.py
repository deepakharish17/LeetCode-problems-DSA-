class Solution(object):
    def isPalindrome(self, head):
    # Create a stack/list and create and set a summy pointer with head
    # add all values in stack
    # now check all stack values is palindrome for that uses temp.val != stack[-1]
    # and traverse the stack and figure it out
        stack=[]
        temp=head
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        temp=head
        while temp is not None:
            if temp.val != stack[-1]:
                return False
            stack.pop()
            temp=temp.next
        return True




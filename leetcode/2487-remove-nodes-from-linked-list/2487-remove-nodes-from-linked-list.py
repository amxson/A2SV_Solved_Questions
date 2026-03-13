# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack =[]
        stack.append(head.val)
        node = head
        while node.next:
            while stack and stack[-1]<node.next.val:
                stack.pop()

            stack.append(node.next.val)
            node = node.next
        dummy = ListNode(0)
        cur = dummy

        for v in stack:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next



            





            


        
# Time Complexity:O(n)
# Space Complexity: O(1)
# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
## Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        curr = head
        while curr!=None:
            #storing my next
            next_node= curr.next
            #change my pointers
            curr.next = prev
            #reset
            prev=curr
            curr=next_node
        return prev

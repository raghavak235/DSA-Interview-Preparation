# Time Complexity:O(n)
# Space Complexity: O(1)
# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        next_ptr = None

        while curr != None:
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr
        head = prev
        return head

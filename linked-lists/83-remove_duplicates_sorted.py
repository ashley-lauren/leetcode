# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        seen_nodes = set()
        node = head
        prev = head

        while node:
            if node.val in seen_nodes:
                prev.next = node.next
            else:
                seen_nodes.add(node.val)
                prev = node
            node = node.next

        return head
        
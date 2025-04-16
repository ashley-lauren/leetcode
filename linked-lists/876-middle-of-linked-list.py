# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        middle_node = head
        end_node = head.next

        while end_node != None:
            middle_node = middle_node.next
            end_node = end_node.next
            if end_node != None:
                end_node = end_node.next

        return middle_node
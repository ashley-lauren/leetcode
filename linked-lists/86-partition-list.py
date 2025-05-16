# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        if not head:
            return 

        first, last = ListNode(0), ListNode(0)
        first_tail, last_tail = first, last

        current = head
        while current:
            next_node = current.next
            current.next = None

            if current.val < x:
                first_tail.next = current
                first_tail = current
            else:
                last_tail.next = current
                last_tail = current

            current = next_node

        first_tail.next = last.next
        head = first.next

        return head
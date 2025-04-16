# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        # we're removing the only node, set head to None
        if head.next == None:
            head = None
            return head

        slow = head
        fast = head
        prev = None

        for _ in range(n):
            if fast == None:
                return None
            fast = fast.next

        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next

        # remove slow from list
        if prev == None:
            head = slow.next
        else:
            prev.next = slow.next

        return head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class AltSolution(object):
    def removeNthFromEnd(self, head, n):
        """
        Improved memory efficiency
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        # we're removing the only node, set head to None
        if not head:
            return None

        slow = head
        fast = head

        for _ in range(n):
            if not fast:
                return None
            fast = fast.next

        # removing head
        if not fast: 
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        # remove slow from list
        slow.next = slow.next.next

        return head
        
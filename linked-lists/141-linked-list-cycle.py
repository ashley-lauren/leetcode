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

        seen_nodes = set()

        curr_node = head
        while(curr_node != None):
            if curr_node in seen_nodes:
                return True
            seen_nodes.add(curr_node)
            curr_node = curr_node.next
        
        return False
    
class AltSolution(object):
    def hasCycle(self, head):
        """
        Solution utilizes tortoise and hare algorithm for better memory complexity
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head
        
        while fast != None:
            slow = slow.next
            fast = fast.next
            
            if (fast == None):
                return False
                
            fast = fast.next
            
            if (slow == fast):
                return True
                
        return False
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getNode(self,node, index):
        while index > 0:
            node = node.next
            index -= 1
        return node
    def getLenNodeList(self, node):
        if (node == None):
            return 0
        len = 1
        while node.next is not None:
            node = node.next
            len +=1
        return len
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getLenNodeList(headA)
        lenB = self.getLenNodeList(headB)
        i = lenA if(lenA<lenB) else lenB
        node = None
        while i > 0:
            nodeA = self.getNode(headA, lenA-1)
            nodeB = self.getNode(headB, lenB-1)
            if nodeA is nodeB:
                # 节点相同
                i -=1
                lenA -=1
                lenB -=1
                node = nodeA
            else:
                break
        return node
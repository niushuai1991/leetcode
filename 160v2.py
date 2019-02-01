# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        startA = headA
        startB = headB
        pointA = headA
        pointB = headB
        # 同时遍历两个链表，找出最短的链表
        while pointA is not None and pointB is not None:
            pointA = pointA.next
            pointB = pointB.next
        # 遍历长的那个链接，将start指针位移到与短的链接相同长度
        if pointA is None:
            while pointB is not None:
                pointB = pointB.next
                startB = startB.next
        else:
            while pointA is not None:
                pointA = pointA.next
                startA = startA.next
        # 从同位开始比较，如果节点相同，则比较完成
        while startA is not None and startB is not None:
            if startA == startB:
                return startA
            else:
                startA = startA.next
                startB = startB.next
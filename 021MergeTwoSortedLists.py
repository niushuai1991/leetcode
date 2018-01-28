'''
Created on 2018年1月25日

@author: niushuai
'''

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "{val:%d}" % self.val

    def print_listnode(self):
        ''' 打印listnode '''
        l = self
        while l != None:
            if l.next == None:
                print(l.val)
            else:
                print("%d->" % l.val, end='')
            l = l.next

def get_list_node(dic):
    root = ListNode(0)
    l = root
    for num in dic:
        l.next = ListNode(num)
        l = l.next
    return root.next

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start_node = ListNode(0)
        current_node = start_node
        while l1 is not None or l2 is not None:
            if l1 == None:
                current_node.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                current_node.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                current_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current_node.next = ListNode(l2.val)
                l2 = l2.next
            current_node = current_node.next
        return start_node.next


if __name__ == '__main__':
    node1 = get_list_node([1,2,4])
    node1.print_listnode()
    node2 = get_list_node([1,3,4])
    node2.print_listnode()
    l3 = Solution().mergeTwoLists(node1, node2)
    l3.print_listnode()

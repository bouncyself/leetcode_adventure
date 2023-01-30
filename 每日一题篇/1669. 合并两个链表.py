# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        now = list1
        i = 0
        while(i < a-1):
            now = now.next
            i+=1
        nodeb = now
        while(i < b+1):
            nodeb = nodeb.next
            i+=1
        flag = True
        if nodeb:
            flag = True
        else:
            flag = False
        now.next = list2
        now = list2
        while(now.next.next):
            now = now.next
        now.next = nodeb
        return list1

if __name__ == '__main__':
    s = Solution()
    list1 = ListNode()
    now = list1
    i=0
    while(i<5):
        now.val = i
        now.next = ListNode()
        now = now.next
        i+=1

    list2 = ListNode()
    now = list2
    i=0
    val = 1000000
    while(i<3):
        now.val = val+i
        now.next = ListNode()
        now = now.next
        i+=1

    s.mergeInBetween(list1 = list1, a = 2, b = 3, list2 = list2)

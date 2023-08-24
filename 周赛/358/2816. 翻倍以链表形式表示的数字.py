# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t = head
        nums = ""
        while t is not None:
            nums+=str(t.val)
            t = t.next
        nums = str(int(nums)*2)
        t = head
        for i in range(len(nums)):
            t.val = int(nums[i])
            if t.next is None and i!=(len(nums)-1):
                t.next = ListNode()
            t = t.next

        return head
'''
题解：
什么时候会受到进位的影响呢？只有下一个节点大于 444 的时候，才会因为进位多加一。

特别地，如果链表头的值大于 444，那么需要在前面插入一个新的节点。
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        cur = head
        while cur:
            cur.val = cur.val * 2 % 10
            if cur.next and cur.next.val > 4:
                cur.val += 1
            cur = cur.next
        return head

作者：灵茶山艾府
链接：https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/solutions/2385962/o1-kong-jian-zuo-fa-kan-cheng-shi-head-y-1dco/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

if __name__ == '__main__':
    s = Solution()
    print(s.doubleIt())


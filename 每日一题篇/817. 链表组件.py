# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        temp = 0
        node_next = head
        flag = True
        while node_next is not None:
            if node_next.val in nums and flag:
                res += 1
                flag = False
            elif node_next.val in nums and not flag:
                pass
            elif node_next.val not in nums:
                flag = True

            node_next = node_next.next
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numComponents())

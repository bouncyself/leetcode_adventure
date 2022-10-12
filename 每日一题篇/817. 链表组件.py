# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
题目：
给定链表头结点head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表nums，该列表是上述链表中整型值的一个子集。

返回列表nums中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表nums中）构成的集合。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/linked-list-components
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
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

#! /usr/bin/env python
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            carry = 0
            ret = ListNode(0)
            ret_last = ret

            while l1 or l2:
                sum_ = 0
                if l1:
                    sum_ = l1.val
                    l1 = l1.next
                if l2:
                    sum_ += l2.val
                    l2 = l2.next
                sum_ += carry
                ret_last.next = ListNode(sum_ % 10)
                ret_last = ret_last.next
                carry = (sum_ >= 10)
            if carry:
                ret_last.next = ListNode(1)
            ret_last = ret.next
            del ret
            return ret_last

if __name__ == '__main__':
    l1 = ListNode([2,3,4])
    l2 = ListNode([4,5,6])
    s = Solution()
    print s.addTwoNumbers(l1, l2)
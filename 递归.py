#! /usr/bin/env python
# -*- coding:utf-8 -*-


def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


class Solution(object):
    def __init__(self):
        pass

    def canPartitionKSubsets(self, nums, k):
        """
        将sums划分成k部分,每部份相加的和都相等
        :param nums:[int, int, int]
        :param k: int
        :return: bool
        """
        target, rem = divmod(sum(nums), k)
        if rem:
            return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group:
                    break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)


if __name__ == '__main__':
    so = Solution()
    print so.canPartitionKSubsets([1, 3, 4, 5, 6, 7, 2], 4)
    import datetime
    t1 = datetime.datetime.now()
    print fac(100 )
    print datetime.datetime.now() - t1
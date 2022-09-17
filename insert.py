"""插入排序+折半插入优化"""

from typing import List
from bisect import bisect


def insertSort(nums: List[int]) -> List[int]:
    """
    插入排序+折半插入优化
    :param nums: 待排序数组
    :return:
    """
    n = len(nums)
    if n < 2:
        return nums

    for i in range(n):
        """[0:i]是排好序的状态"""
        tmp = nums[:i]
        j = bisect(tmp, nums[i])

        tmp.insert(j, nums[i])
        nums = tmp + nums[i + 1:]
    return nums


if __name__ == "__main__":
    nums = [5, 2, 3, 1, 6, 5, 4]
    res = insertSort(nums)
    print(res)

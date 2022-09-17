"""冒泡排序+提前优化"""

from typing import List


def bubbleSort(nums: List[int]) -> List[int]:
    """
    冒泡排序
    :param nums: 待排序数组
    :return: 排好序的数组
    """

    n = len(nums)
    if n < 2:
        return nums

    for i in range(n):
        swap = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = True

        if not swap:
            break

    return nums


if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    res = bubbleSort(nums)
    print(res)

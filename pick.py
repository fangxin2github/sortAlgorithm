"""选择排序"""

from typing import List


def pickSort(nums: List[int]) -> List[int]:
    """
    选择排序+双元优化 一次迭代找到最大值和最小值
    :param nums: 待排序数组
    :return:
    """
    n = len(nums)
    if n < 2:
        return nums

    min_idx = 0
    max_idx = n - 1

    for i in range(n // 2):
        min_tmp = min_idx
        max_tmp = max_idx
        for j in range(i, n - i):
            if nums[j] < nums[min_tmp]:
                min_tmp = j
            if nums[j] > nums[max_tmp]:
                max_tmp = j
        nums[min_idx], nums[min_tmp] = nums[min_tmp], nums[min_idx]
        nums[max_idx], nums[max_tmp] = nums[max_tmp], nums[max_idx]

        min_idx += 1
        max_idx -= 1
    return nums


if __name__ == "__main__":
    nums = [0, 1, 1, 2, 5, 0]
    res = pickSort(nums)
    print(res)

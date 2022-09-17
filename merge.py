"""归并排序"""


def Merge(A, p, q, r):
    """合并两个排好序的数组"""
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = A[p + i - 1]
    for j in range(n2):
        R[j] = A[q + j]
    i, j = 0, 0
    for k in range(p - 1, r):
        if i >= n1:
            A[k] = R[j]
            j += 1
        elif j >= n2:
            A[k] = L[i]
            i += 1
        elif L[i] >= R[j]:
            A[k] = R[j]
            j += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
    return A


def MergeSort(A, p, r):
    """自顶向下的归并排序"""
    if p < r:
        q = int((p + r) / 2)
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)

    return A


if __name__ == "__main__":
    nums = [5, 2, 3, 1, 6, 5, 4]
    res = MergeSort(nums, 1, len(nums))
    print(res)



from typing import List


def quicksort(nums: List[int]) -> List[int]:
    len_nums = len(nums)

    if len_nums < 2:
        return nums

    pivot_index = int(len_nums / 2)
    pivot = nums[pivot_index]
    less: List[int] = []
    greater: List[int] = []

    for i, n in enumerate(nums):
        if i == pivot_index:
            continue
        _append = greater.append if n > pivot else less.append
        _append(n)

    return quicksort(less) + [pivot] + quicksort(greater)

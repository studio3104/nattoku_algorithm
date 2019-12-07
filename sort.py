from typing import List


def quicksort(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums

    pivot = nums[0]
    less: List[int] = []
    greater: List[int] = []

    for n in nums[1:]:
        _append = greater.append if n > pivot else less.append
        _append(n)

    return quicksort(less) + [pivot] + quicksort(greater)

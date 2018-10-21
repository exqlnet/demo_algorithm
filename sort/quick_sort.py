from random import randint
nums = [5, 3, 7]


def qsort(nums):
    if len(nums) <= 1: # 基线条件
        return nums

    left = []
    right = []
    standard = nums.pop(randint(0, len(nums) - 1))
    for n in nums:
        if n <= standard:
            left.append(n)
        elif n > standard:
            right.append(n)

    return qsort(left) + [standard] + qsort(right)


print(qsort(nums))

from decorator import runtime
a = [3, 5, 2, 4, 7, 1]


def swap(l, x, y):
    t = l[x]
    l[x] = l[y]
    l[y] = t


@runtime
def select_sort(nums):
    length = len(nums)
    for i in range(length):
        for j in range(i, length):
            if nums[j] < nums[i]:
                swap(nums, i, j)
    return nums


print(select_sort(a))


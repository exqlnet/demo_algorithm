nums = [1, 3, 2, 5, 6, 7, 8, 9, 10, 11]
from sort.decorator import runtime


def time_count(func):
    t = 0

    def wrapper(*args, **kwargs):
        nonlocal t
        t += 1
        print("Already count {} times.".format(t))
        return func(*args, **kwargs)
    return wrapper


times = 0


def all_rank(nums, i):
    if i == len(nums):
        global times
        times += 1
    else:
        for n in range(i, len(nums)):
            t = nums[i]
            nums[i] = nums[n]
            nums[n] = t
            all_rank(nums, i + 1)
            t = nums[i]
            nums[i] = nums[n]
            nums[n] = t


import time

t1 = time.time()
all_rank(nums, 0)

t2 = time.time()

print("Running time {}s.".format(t2 - t1))
print("Already find {}.".format(times))

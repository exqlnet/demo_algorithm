import time


def runtime(func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        nums = func(*args, **kwargs)
        t2 = time.time()
        print("{}耗时{}".format(func.__name__, t2 - t1))
        return nums

    return wrapper

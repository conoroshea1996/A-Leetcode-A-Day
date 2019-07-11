import math


def sqaure(nums):
    arr = sorted(nums)
    sqaured = []
    for i in arr:
        sqaured.append(i * i)

    result = sorted(sqaured)

    return result


print(sqaure([-4, -1, 0, 3, 10]))

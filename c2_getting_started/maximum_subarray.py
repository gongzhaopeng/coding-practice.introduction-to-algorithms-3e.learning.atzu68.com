import math


def __find_max_crossing_subarray(array, low, mid, high):
    left_sum = -math.inf
    max_left = mid - 1
    s = 0
    for i in range(mid - 1, low - 1, -1):
        s += array[i]
        if s > left_sum:
            left_sum = s
            max_left = i
    right_sum = -math.inf
    max_right = mid
    s = 0
    for j in range(mid, high):
        s += array[j]
        if s > right_sum:
            right_sum = s
            max_right = j
    return max_left, max_right + 1, left_sum + right_sum


def __find_maximum_subarray(array, low, high):
    if high - low < 2:
        return low, high, array[low]

    mid = int((low + high) / 2)
    _, _, left_sum = left_solution = __find_maximum_subarray(array, low, mid)
    _, _, right_sum = right_solution = __find_maximum_subarray(array, mid, high)
    _, _, cross_sum = cross_solution = __find_max_crossing_subarray(array, low, mid, high)

    if right_sum > left_sum:
        if right_sum > cross_sum:
            return right_solution
        else:
            return cross_solution
    elif left_sum < cross_sum:
        return cross_solution
    else:
        return left_solution


def find_maximum_subarray(array):
    return __find_maximum_subarray(array, 0, len(array))

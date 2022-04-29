import math


def __merge(array, p, q, r):
    left = array[p:q]
    left.append(math.inf)
    right = array[q:r]
    right.append(math.inf)

    i = j = 0
    for k in range(p, r):
        if left[i] > right[j]:
            array[k] = right[j]
            j += 1
        else:
            array[k] = left[i]
            i += 1


def __merge_sort(array, p, r):
    if r - p > 1:
        q = int((p + r) / 2)
        __merge_sort(array, p, q)
        __merge_sort(array, q, r)
        __merge(array, p, q, r)


def merge_sort(array):
    __merge_sort(array, 0, len(array))

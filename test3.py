def bubble_sort(alist):
    """冒泡排序"""
    for j in range(len(alist)-1, 1, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
    alist = [2, 5, 28, 18, 9, 3]
    bubble_sort(alist)
    print(alist)


# def select_sort(alist):
#     """选择排序"""
#     for i in range(len(alist)-1):
#         min_index = i
#         for j in range(i+1, len(alist)):
#             if alist[j] < alist[min_index]:
#                 min_index = j
#         if min_index != i:
#             alist[i], alist[min_index] = alist[min_index], alist[i]
#
#
# if __name__ == '__main__':
#     alist = [2, 5, 28, 18, 9, 3]
#     select_sort(alist)
#     print(alist)

# def insert_sort(alist):
#     """插入排序"""
#     for i in range(1, len(alist)):
#         for j in range(i, 0, -1):
#             if alist[j] < alist[j-1]:
#                 alist[j], alist[j-1] = alist[j-1], alist[j]
#
#
# if __name__ == '__main__':
#     alist = [2, 5, 28, 18, 9, 3]
#     insert_sort(alist)
#     print(alist)


# def shell_sort(alist):
#     """希尔排序"""
#     gap = len(alist) // 2
#     while gap > 0:
#         for i in range(gap, len(alist)):
#             j = i
#             while j >= gap and alist[j-gap] > alist[j]:
#                 alist[j-gap], alist[j] = alist[j], alist[j-gap]
#                 j -= gap
#
#         gap = gap // 2
#
#
# if __name__ == '__main__':
#     alist = [2, 5, 28, 18, 9, 3]
#     shell_sort(alist)
#     print(alist)


# def quick_sort(alist, start, end):
#     """快速排序"""
#     if start >= end:
#         return
#     mid = alist[start]
#     low = start
#     high = end
#     while low < high:
#         while low < high and alist[high] >= mid:
#             high -= 1
#         alist[low] = alist[high]
#
#         while low < high and alist[low] < mid:
#             low += 1
#         alist[high] = alist[low]
#     alist[low] = mid
#
#     quick_sort(alist, start, low-1)
#     quick_sort(alist, low+1, end)
#
#
# if __name__ == '__main__':
#     alist = [2, 5, 28, 18, 9, 3]
#     quick_sort(alist, 0, len(alist)-1)
#     print(alist)

def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    num = len(alist) / 2
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])

    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        result += left[l:]
        result += right[r:]
        return result


if __name__ == '__main__':
    alist = [2, 5, 28, 18, 9, 3]
    sorted_list = merge_sort(alist)
    print(sorted_list)

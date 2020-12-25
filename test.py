def fun(alist, star, end):
    # for i in range(len(alist)-1, 0, -1):
    #     for j in range(i):
    #         if alist[j] > alist[j+1]:
    #             alist[j], alist[j+1] = alist[j+1], alist[j]


    # for i in range(len(alist)-1):
    #     min_index = i
    #     for j in range(i+1, len(alist)):
    #         if alist[j] < alist[min_index]:
    #             min_index = j
    #
    #     if min_index != i:
    #         alist[i], alist[min_index] = alist[min_index], alist[i]

    # for i in range(1, len(alist)):
    #     for j in range(i, 0, -1):
    #         if alist[j] < alist[j-1]:
    #             alist[j], alist[j-1] = alist[j-1], alist[j]

    if star >= end:
        return

    mid = alist[star]
    low = star
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1

        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1

        alist[high] = alist[low]

    alist[low] = mid
    fun(alist, star, low-1)
    fun(alist, low+1, end)


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fun(li, 0, len(li)-1)
print(li)


import random
# print(sorted([i for i in range(10)], key=lambda i: i[0]))
# print(set([i for i in range(10)]))
# list = [i for i in range(10, 20)]
# print(list)
# list2 = []
# while True:
#     for i in list:
#         a = random.randint(0, len(list)-1)
#         if list[a] not in list2:
#             list2.append(list[a])
#     if len(list) == len(list2):
#         break
# print(list2)
# list = [i for i in range(10)]
# random.shuffle(list)
# random._urandom
# list2 = sorted(list, key=lambda a: random.random())
# print(list2)
# print(list)
# g = (i for i in range(10))
# print(type(g))


# str = 'hello world ha ha'
# print(str.split())
# def bubble_sort(alist):
#     """冒泡排序"""
#     for j in range(len(alist)-1, 1, -1):
#         for i in range(j):
#             if alist[i] > alist[i+1]:
#                 alist[i], alist[i+1] = alist[i+1], alist[i]
#
#
# if __name__ == '__main__':
#     alist = [2, 5, 28, 18, 9, 3]
#     bubble_sort(alist)
#     print(alist)

def bubble_sort(str1):
    for i in str1:
        if str1.count(i) == 1:
            return str1.index(i)


str1 = 'aabbcddceie'
res = bubble_sort(str1)
print(res)

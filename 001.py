# class Singleton:
#     __isinstance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__isinstance:
#             cls.__isinstance = object.__new__(cls)
#         return cls.__isinstance


# str = 'I am a boy'
# list1 = str.split(' ')
# list1.reverse()
# str2 = ' '.join(list1)
# print(str2)

# str = 'abaca'
# res = len(set(str))
# print(res)
# sushu = []
# for i in range(100, 201):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         if i == j + 1:
#             sushu.append(i)
# print(sushu)
# class Singleton:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance

# lsit1 = [[x, x+1, x+2] for x in range(1, 100, 3)]
# print(lsit1)
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = [[list1[x], list1[x+1], list1[x+2]] for x in range(0, 9, 3)]
# print(list2)

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# c = consumer()
# produce(c)

import asyncio


@asyncio.coroutine
def hello():
    print('hello world')
    r = yield from asyncio.sleep(1)
    print('hello again')


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
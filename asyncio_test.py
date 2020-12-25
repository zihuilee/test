import asyncio
import random
import threading
from aiohttp import web
from multiprocessing import Queue, Process
import os, time
import threading
import re


class Foo(object):
    def func(self):
        pass

    
print(Foo.__doc__)
# str1 = '<html>hh</html>'
# res = re.match(r'<([a-zA-Z]*)>\w*</\1>', str1)
# if res:
#     print(res.group())


# local_school = threading.local()
#
#
# def process_student():
#     # 获取当前线程关联的student
#     stu = local_school.student
#     print('Hello, %s (in %s)' % (stu, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadingLock的student
#     local_school.student = name
#     process_student()
#
#
# p1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# p2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# p1.start()
# p2.start()
# p1.join()
# p2.join()


# def write(q):
#     print('Process to write:%s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()


# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>')
#
#
# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello %s</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))
#
#
# async def init(loop):
#     app = web.Application()
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server('127.0.0.1', 8000)
#     print('server started at http://127.0.0.1/8000')
#     return srv
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init())
# loop.run_forever()

# @asyncio.coroutine
# def wget():
#     print("hello world %s" % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print("hello again %s" % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(), wget()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# async def hello():
#     print('hello world')
#     r = await asyncio.sleep(1)
#     print('hello again!')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

# @asyncio.coroutine
# def wget(host):
#     print('wget %s' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# async def wget(host):
#     print('wget %s' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = await connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     await writer.drain()
#     while True:
#         line = await reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()



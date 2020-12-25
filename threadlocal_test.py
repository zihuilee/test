import threading

loacl_school = threading.local()


def process_student():
    std = loacl_school.student
    print('helo, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    loacl_school.student = name

    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

from time import ctime, sleep


def timefun(func):
    def wrapped_func():
        print('%s called at %s' % (func.__name__, ctime()))
        func()

    return wrapped_func


@timefun
def foo():
    print('i am do')


foo()
sleep(2)
foo()

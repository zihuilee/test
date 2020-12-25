from threading import Timer
import time


def time_limit(interval):
    def wraps(func):
        def time_out():
            try:
                raise RuntimeError()
            except Exception as e:
                print('运行超时')
            return

        def deso(*args, **kwargs):
            timer = Timer(interval, time_out)
            timer.start()
            func(*args, **kwargs)
            timer.cancel()
        return deso
    return wraps


@time_limit(9)
def func():
    time.sleep(10)
    print('hello python')


func()


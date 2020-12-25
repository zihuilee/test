import threading
from time import sleep,ctime


def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)


def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)


if __name__ == '__main__':
    print('---开始---:%s'%ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # sleep(5) # 屏蔽此行代码，试试看，程序是否会立马结束？
    print('---结束---:%s' % ctime())
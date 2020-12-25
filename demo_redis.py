from redis import *


if __name__ == '__main__':
    try:
        sr = StrictRedis(host='localhost', port=6379, db=1)
        result = sr.keys()
        for i in result:
            print(i.decode())

    except Exception as e:
        print(e)

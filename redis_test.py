from redis import *


if __name__ == '__main__':
    try:
        sr = StrictRedis(host='', port=6379, db=1)
        # res = sr.set('name', 'itcast')
        # res = sr.get('name')
        # print(res.decode('utf-8'))
        # res = sr.set('name', 'itcast1')
        # res = sr.delete('name')
        res = sr.keys()
        for i in res:
            print(i.decode('utf-8'))
    except Exception as e:
        print(e)


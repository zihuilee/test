# def dict_updater(k, v, dic={}):
#     dic[k] = v
#     print(dic)
#
#
# dict_updater('one', 1)
# dict_updater('two', 2)
# dict_updater('three', 3, {})


def say_hi(func):
    def wrapper(*args, **kwargs):
        print('Hi')
        ret = func(*args, **kwargs)
        print('Bye')
        return ret
    return wrapper


def say_yo(func):
    def wrapper(*args, **kwargs):
        print('Yo')
        return func(*args, **kwargs)
    return wrapper


@say_hi
@say_yo
def func():
    print('Rock & Roll')

# Hi Bye Yo Rock Roll


func()


# def test():
#     try:
#         raise ValueError('Something Wrong!')
#     except ValueError as e:
#         print('Error occurred!')
#         return
#     finally:
#         print('Done')
#
#
# test()


# class Singleton:
#     _isinstance = None
#
#     def __new__(cls, *args, **kwargs):
#         print('New')
#         if cls._isinstance is None:
#             print('Create')
#             cls._isinstance = super().__new__(cls, *args, **kwargs)
#         return cls._isinstance
#
#     def __init__(self):
#         print('Initialize')
#         self.prop = None
#
#
# s1 = Singleton()
# s2 = Singleton()

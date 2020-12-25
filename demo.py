class A:
    def __init__(self):
        print('init方法')

    def __new__(cls, *args, **kwargs):
        print('new方法')
        return object.__new__(cls)


a = A()

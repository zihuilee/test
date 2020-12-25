def createCounter():

    def add_nums():
        n = 0
        while True:
            n += 1
            yield n
    y = add_nums()

    def counter():
        return next(y)
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA())

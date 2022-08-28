
def add_some_feature(fn):
    def wrapper(*args, **kwargs):
        print("Какой-то текст до (1)")
        print("Какой-то текст до (2)")
        fn(*args, **kwargs)
        print("Какой-то текст после")
    return wrapper


@add_some_feature
def sum(a, b):
    c = a + b
    return c


@add_some_feature
def something():
    n = 7
    print(7)


something()
#
# d = sum(7, 2)
# print(d)

def foo(a, b=0, *args, **kwargs):
    print(a, b, args, kwargs)


tup = (1, 2, 3, 4)
lst = [1, 2, 3, 4]
d = {'e':1, 'f':2, 'g':'3'}


foo(1, *tup, b=5)
foo(1, b=5, *tup)

foo(1, *tup, b=5)
foo(1, b=5, *tup)


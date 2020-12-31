def f(x):
    return 2 * x + 7


def g(x):
    return x ** 2


x = 2
print(f(x) + g(x) + f(g(x)) + g(f(x)))

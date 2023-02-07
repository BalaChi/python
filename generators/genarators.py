# all gnerators are iterables but all iterable are not generators


def generators_func(num):
    for i in range(num):
        yield i

g = generators_func(1)

for i in generators_func(100):
    print(i)



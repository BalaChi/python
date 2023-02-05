from time import time
def performance(fn):
    def wrapper():
        t1 = time()
        result = fn()
        t2 = time()
        print(f'took {t2-t1}')
        return result
    return wrapper
@performance
def longtime():
    for i in range(100000):
        i * 5

longtime()
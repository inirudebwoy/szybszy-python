from timeit import Timer

if __name__ == "__main__":
    t = Timer('fib_cython.fib(10)', 'import fib_cython')
    print t.repeat(3)

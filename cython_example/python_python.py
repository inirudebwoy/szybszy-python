from timeit import Timer


def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    #while b < n:
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    t = Timer('fib(10)', 'from __main__ import fib')
    print t.repeat(3)

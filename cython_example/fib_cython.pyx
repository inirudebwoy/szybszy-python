def fib(int n):
#def fib(n):
    """Print the Fibonacci series up to n."""
    cdef int a
    cdef int b
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

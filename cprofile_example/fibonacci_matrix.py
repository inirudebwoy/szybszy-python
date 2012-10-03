# Copyright (c) 2012 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Fibonacci_numbers_(Python)?action=history&offset=20120313200633
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Retrieved from: http://en.literateprograms.org/Fibonacci_numbers_(Python)?oldid=18052


def mul(A, B):
    a, b, c = A
    d, e, f = B
    return (a * d + b * e,
            a * e + b * f,
            b * e + c * f)


def pow(A, n):
    if n == 1:
        return A
    if n & 1 == 0:
        return pow(mul(A, A), n // 2)
    else:
        return mul(A, pow(mul(A, A), (n - 1) // 2))


def fib(n):
    if n < 2:
        return n
    return pow((1, 1, 0), n - 1)[0]

if __name__ == "__main__":
    fib(1000000)

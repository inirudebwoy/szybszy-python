#include "builtin.hpp"
#include "shedskin.hpp"

namespace __shedskin__ {

str *const_0;


str *__name__;



__ss_int fib(__ss_int n) {
    /**
    Print the Fibonacci series up to n.
    */
    __ss_int __0, __1, a, b;

    a = 0;
    b = 1;

    while ((b<n)) {
        __0 = b;
        __1 = (a+b);
        a = __0;
        b = __1;
    }
    return a;
}

void __init() {
    const_0 = new str("__main__");

    __name__ = new str("__main__");

    if (__eq(__name__, const_0)) {
        fib(100000);
    }
}

} // module namespace

int main(int, char **) {
    __shedskin__::__init();
    __shedskin__::__start(__shedskin__::__init);
}

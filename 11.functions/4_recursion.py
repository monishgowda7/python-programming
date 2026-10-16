# fibonacci number
# 0 1 1 2 3 5 8 13 21
# 0 1 2 3 4 5 6 7  8  

# fibonacci number is addition of 1st two fibonacci number

# fib(0)=0
# fib(1)=1
# fib(2)=fib(0)+fib(1)
# fib(3)=fib(2)+fib(1)
# fib(4)=fib(3)+fib(2) 
# fib(n)=fib(n-2)+fib(n-1)


def fib(n):
    if (n == 0 or n == 1):
        return n

    return fib(n - 2) + fib(n - 1)


print(fib(6))


fib(6)
fib(4) + fib(5)
fib(2) + fib(3) + fib(3) + fib(4)
1 + 0 + 1 + fib(2) + 1 + fib(2) + fib(2) + fib(3)
1 + 0 + 1 + fib(1) + fib(0) + 1 + fib(1) + fib(0) + fib(1) + fib(0) + fib(1) + fib(2)
1 + 0 + 1 + 1 + fib(0) + 1 + 1 + fib(0) + 1 + fib(0) + 1 + fib(1) + fib(0)
1 + 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0

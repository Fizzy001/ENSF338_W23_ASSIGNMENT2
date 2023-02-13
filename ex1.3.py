# Using memoization to implement the code above

term = [0 for i in range(1000)]

def fib(n):
    if n == 0 or n ==1:
        return n
    else:
        term[n] = fib(n-1) + fib(n-2)
        return term[n]
#Timing the original code
import timeit
#Fibonacci function using recursion 



code_to_test= """def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
func(35)
"""

elapsed_time = timeit.timeit(code_to_test, number=1)
print("Time elapsed: ", elapsed_time, "seconds")




#Timig the improved code
 
#Using memoization to implement the code
code_to_test= """def fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
fib(35)
"""

elapsed_time = timeit.timeit(code_to_test, number=1)
print("Time elapsed: ", elapsed_time, "seconds")

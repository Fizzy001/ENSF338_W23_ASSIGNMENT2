#Timing the original code
import timeit
#Fibonacci function using recursion




code_to_test= """def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
func(0)
"""
 
elapsed_time = timeit.timeit(code_to_test, number=1)
print("Time elapsed original code: ", elapsed_time, "seconds")






#Timig the improved code
#Using memoization to implement the code
code_to_test= """term = [0 for i in range(1000)]
 
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        term[n] = fib(n-1)+fib(n-2)
        return term[n]
fib(0)
"""
 
elapsed_time = timeit.timeit(code_to_test, number=1)
print("Time elapsed improved code: ", elapsed_time, "seconds")
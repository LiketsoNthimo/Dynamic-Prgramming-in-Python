"""
Fibonnaci recursion lecture example
"""

def fib(n):
    print("Fib compute: " + str(n))
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(str(fib(6)))
print(str(fib(7)))
print(str(fib(8)))
print(str(fib(50)))


"""
Fibonnaci memoization lecture example
"""

def fib(n, memo_list = {}):
    if n in memo_list:
        return memo_list[n]
    
    if n <= 2:
        return 1
    
    else:
        memo_list[n] = fib(n-1, memo_list) + fib(n-2, memo_list)
        return memo_list[n]
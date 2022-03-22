"""
Fibonacci lecture adaption
"""

def fib(n):
    
    table = [0] * (n+1)
    table[1] = 1
    
    for i in range(n):
        if i == n-1:
            return table[n] + table[i]
        
        table[i+1] += table[i]
        table[i+2] += table[i]
        
    return table[n]

print(str(fib(5)))
print(str(fib(7)))
print(str(fib(8)))
print(str(fib(50)))

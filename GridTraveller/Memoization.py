"""
gridTraveller recursion lecture example
"""

def gridTraveller(n, m):
    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    else:
        return gridTraveller(n - 1, m) + gridTraveller(n, m - 1)
    
print(str(gridTraveller(1,1)))
print(str(gridTraveller(2,3)))
print(str(gridTraveller(4,4)))
print(str(gridTraveller(18,18)))


"""
gridTraveller memoization lecture example
"""

def gridTraveller(n, m, memo_list = {}):
    key = str(n) + "," + str(m)
    print("grid compute: " + key)
    reverse_key = str(m) + "," + str(n)
    
    if key in memo_list:
        print("stored compute: " + key)
        return memo_list[key]
    
    if reverse_key in memo_list:
        return memo_list[reverse_key]
    
    if n == 1 and m == 1:
        return 1
    
    if n == 0 or m == 0:
        return 0
    
    else:
        memo_list[key] = gridTraveller(n - 1, m, memo_list) + gridTraveller(n, m - 1, memo_list)
        memo_list[reverse_key] = memo_list[key]
        return memo_list[key]

"""
Grid traveller lecture example
"""

def gridTraveller(m, n):
    sub_table = [0] * (m+1)
    table = list(map(lambda x: [x] * (n+1), sub_table))
    
    table[1][1] = 1
    
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j+1 <= n:
                table[i][j+1] += current
            if i+1 <= m:
                table[i+1][j] += current
    
    return table[m][n]


print(str(gridTraveller(1,1)))
print(str(gridTraveller(2,3)))
print(str(gridTraveller(3,2)))
print(str(gridTraveller(3,3)))
print(str(gridTraveller(18,18)))
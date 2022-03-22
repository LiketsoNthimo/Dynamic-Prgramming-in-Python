"""
Can Sum lecture example
"""

def canSum(targetSum, numbers):
    table = [False] * (targetSum + 1)
    
    table[0] = True
    
    for i in range(targetSum):
        if table[i]:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = True
    
    return table[targetSum]

print(str(canSum(7, [2,4])))
print(str(canSum(8, [2,3,5])))
print(str(canSum(300, [7,14])))
"""
Best Sum lecture example
"""

def bestSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    
    table[0] = []
    
    for i in range(targetSum):
        if table[i] != None:
            for num in numbers:
                if i + num <= targetSum:
                    combination = table[i] + [num]
                    
                    if table[i + num] == None or len(combination) < len(table[i + num]):
                        table[i + num] = combination
    
    return table[targetSum]

print(str(bestSum(7, [5, 3, 4, 7])))
print(str(bestSum(8, [2,3,5])))
print(str(bestSum(8, [1,4,5])))
print(str(bestSum(100, [1,2,5,25])))
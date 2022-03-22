"""
HowSum lecture adaptation
"""

def howSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    
    table[0] = []
    
    for i in range(targetSum):
        if table[i] != None:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = table[i] + [num]
    
    return table[targetSum]

print(str(howSum(7, [2, 3])))
print(str(howSum(7, [5, 3, 4, 7])))
print(str(howSum(7, [2, 4])))
print(str(howSum(8, [2, 3, 5])))
print(str(howSum(300, [7,14])))
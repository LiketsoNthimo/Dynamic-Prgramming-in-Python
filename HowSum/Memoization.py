"""
howSum memoization lecture example
"""

def howSum(targetSum, numbers, memo_list = {}):
    if targetSum in memo_list:
        return memo_list[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo_list)
        
        if remainderResult != None:
            remainderResult.append(num)
            memo_list[targetSum] = remainderResult
            return remainderResult
    
    memo_list[remainderResult] = None
    return None

""" Remember to remove variables before running each test"""
print(str(howSum(7, [2,4])))
print(str(howSum(8, [2,3,5])))
print(str(howSum(300, [7,14])))
"""
canSum recursion lecture example
"""

def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    
    if targetSum < 0:
        return False
    
    for num in numbers:
        remainder = targetSum - num
        
        if canSum(remainder, numbers):
            return True
    
    return False


print(str(canSum(8, [2,3,5])))
print(str(canSum(300, [7,14])))


"""
canSum memoization lecture example
"""

def canSum(targetSum, numbers, memo_list = {}):
    if targetSum in memo_list:
        return memo_list[targetSum]
    
    if targetSum == 0:
        return True
    
    if targetSum < 0:
        return False
    
    for num in numbers:
        remainder = targetSum - num
        
        if canSum(remainder, numbers, memo_list):
            memo_list[targetSum] = True
            return True
    
    memo_list[targetSum] = False
    return False

""" Remember to remove variables before running each test"""
print(str(canSum(7, [2,4])))
print(str(canSum(8, [2,3,5])))
print(str(canSum(300, [7,14])))

"""
bestSum recursion lecture example
"""

def bestSum(targetSum, numbers):        
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination != None:
            combination = remainderCombination.copy()
            combination.append(num)
            
            if shortestCombination == None or len(combination) < len(shortestCombination):
                shortestCombination = combination
    
    return shortestCombination


"""
bestSum memoization lecture example
"""

def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination != None:
            combination = remainderCombination.copy()
            combination.append(num)
            
            if shortestCombination == None or len(combination) < len(shortestCombination):
                shortestCombination = combination
    
    memo[targetSum] = shortestCombination
    return shortestCombination


""" Remember to remove variables before running each test"""
print(str(bestSum(7, [5, 3, 4, 7])))
print(str(bestSum(8, [2,3,5])))
print(str(bestSum(8, [1,4,5])))
print(str(bestSum(100, [1,2,5,25])))
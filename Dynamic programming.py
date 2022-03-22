# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 23:17:43 2021

@author: nthimol01
"""

    
"""
FIBONACCI
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
MEMOIZATION fibonacci
"""


def fib(n, memo_list = {}):
    if n in memo_list:
        return memo_list[n]
    
    if n <= 2:
        return 1
    
    else:
        memo_list[n] = fib(n-1, memo_list) + fib(n-2, memo_list)
        return memo_list[n]
    
"""
Grid traveller
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
MEMOIZATION Grid traveller
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


"""
CanSum own implementation
"""

def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    
    if targetSum < min(numbers):
        return False
    
    truth_list = [False] * len(numbers)
    for i in range(len(numbers)):
        truth_list[i] = canSum(targetSum - numbers[i], numbers)
    
    if True in truth_list:
        return True
    else:
        return False

canSum(7,[2,3])


"""
canSum lecture example
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
canSum lecture example memoize
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



"""
howSum own example
"""

def howSum(targetSum, numbers):
    print("new target sum: " + str(targetSum))
    if targetSum == 0:
        return []
    
    if targetSum < min(numbers):
        return None
    
    for num in numbers:
        remainder = targetSum - num
        print("Remainder value: " + str(remainder))
        howSumValue = howSum(remainder, numbers)
        print("howSumValue: " + str(howSumValue))
        if howSumValue != None:
            #return howSumValue.append(num)
            howSumValue.append(num)
            print("howSumValue: " + str(howSumValue))
            return howSumValue
    
    return None


def howSum(targetSum, numbers, memo_list = {}):
    if targetSum in memo_list:
        return memo_list[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < min(numbers):
        return None
    
    for num in numbers:
        remainder = targetSum - num
        howSumValue = howSum(remainder, numbers, memo_list)
        if howSumValue != None:
            howSumValue.append(num)
            memo_list[targetSum] = howSumValue
            return howSumValue
    
    memo_list[targetSum] = None
    return None

print(str(howSum(7, [2,3])))
print(str(howSum(300, [7,14])))


"""
howSum lecture example memoize
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


"""
bestSum own example
"""

def bestSum(targetSum, numbers):
    print("new target sum: " + str(targetSum))
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    bestSumValueLength = targetSum + 1 #targetSum/min(numbers) + 1
    bestSumValue = None
    
    for num in numbers:
        remainder = targetSum - num
        print("Remainder value: " + str(remainder))
        #print("bestSumValue: " + str(bestSumValue))
        if bestSum(remainder, numbers) != None and len(bestSum(remainder, numbers)) < bestSumValueLength:
            #return howSumValue.append(num)
            bestSumValue = bestSum(remainder, numbers)
            bestSumValueLength = len(bestSumValue)
            bestSumValue.append(num)
            print("bestSumValue: " + str(bestSumValue))
    
    print("Loop end bestSumValue: " + str(bestSumValue))
    if bestSumValue == None:
        return None
    else:
        return bestSumValue

def bestSum(targetSum, numbers):
    print("new target sum: " + str(targetSum))
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    bestSumValueLength = targetSum + 1 #targetSum/min(numbers) + 1
    bestSumValue = None
    
    for num in numbers:
        remainder = targetSum - num
        print("Remainder value: " + str(remainder))
        interimBestSumValue = bestSum(remainder, numbers)
        print("interimBestSumValue: " + str(interimBestSumValue))
        if interimBestSumValue != None and len(interimBestSumValue) < bestSumValueLength:
            #return howSumValue.append(num)
            bestSumValueLength = len(interimBestSumValue)
            interimBestSumValue.append(num)
            bestSumValue = interimBestSumValue.copy()
            print("bestSumValue: " + str(bestSumValue))
    
    print("Loop end bestSumValue: " + str(bestSumValue))
    return bestSumValue

print(str(bestSum(8, [1,4,5])))


def bestSum(targetSum, numbers, memo_list = {}):
    print("new target sum: " + str(targetSum))
    if targetSum in memo_list:
        print("memo at target sum: " + str(targetSum))
        return memo_list[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    bestSumValueLength = targetSum + 1 #targetSum/min(numbers) + 1
    bestSumValue = None
    
    for num in numbers:
        remainder = targetSum - num
        print("Remainder value: " + str(remainder))
        interimBestSumValue = bestSum(remainder, numbers, memo_list)
        print("interimBestSumValue: " + str(interimBestSumValue))
        if interimBestSumValue != None and len(interimBestSumValue) < bestSumValueLength:
            #return howSumValue.append(num)
            bestSumValueLength = len(interimBestSumValue)
            interimBestSumValue.append(num)
            bestSumValue = interimBestSumValue.copy()
            print("bestSumValue: " + str(bestSumValue))
    
    print("Loop end bestSumValue: " + str(bestSumValue))
    memo_list[targetSum] = bestSumValue
    return bestSumValue



""" Remember to remove variables before running each test"""
print(str(bestSum(7, [5, 3, 4, 7])))
print(str(bestSum(8, [2,3,5])))
print(str(bestSum(8, [1,4,5])))
print(str(bestSum(100, [1,2,5,25])))


"""
bestSum lecture example
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


"""Memoisation"""

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



"""
canConstruct own example
"""

def canConstruct(target, wordBank):
    if target == '':
        return True
    
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            canConstrunctValue = canConstruct(target[wordLength:],wordBank)
            if canConstrunctValue:
                return True
            
    return False

""" Memoization """

def canConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    
    if target == '':
        return True
    
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            canConstrunctValue = canConstruct(target[wordLength:],wordBank)
            if canConstrunctValue:
                memo[target] = True
                return True
    
    memo[target] = False        
    return False

print(str(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])))
print(str(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(str(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])))
print(str(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))


"""
canConstruct lecture adaptation example
"""

def canConstruct(target, wordBank):
    if target == '':
        return True
    
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            if canConstruct(suffix, wordBank):
                return True
            
    return False

""" Memoization """

def canConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    
    if target == '':
        return True
    
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True
    
    memo[target] = False        
    return False

print(str(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])))
print(str(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(str(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])))
print(str(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))

"""
countConstruct own example
"""

def countConstruct(target, wordBank):
    if target == '':
        return 1
    
    targetWays = 0
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            suffixWays = countConstruct(suffix, wordBank)
            targetWays = targetWays + suffixWays
    
    return targetWays

""" Memoization """

def countConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    
    if target == '':
        return 1
    
    targetWays = 0
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            suffixWays = countConstruct(suffix, wordBank, memo)
            targetWays = targetWays + suffixWays
    
    memo[target] = targetWays
    return targetWays


"""
countConstruct lecture example
"""

def countConstruct(target, wordBank):
    if target == '':
        return 1
    
    totalCount = 0
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            numWaysForRest = countConstruct(suffix, wordBank)
            totalCount += numWaysForRest
    
    return totalCount

""" Memoization """

def countConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    
    if target == '':
        return 1
    
    totalCount = 0
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            numWaysForRest = countConstruct(suffix, wordBank, memo)
            totalCount += numWaysForRest
    
    memo[target] = totalCount
    return totalCount

print(str(countConstruct("abana", ["ab", "a", "an", "na", "abcd"])))
print(str(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])))
print(str(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])))
print(str(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(str(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])))
print(str(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))


"""
allConstruct own example
"""

def allConstruct(target, wordBank):
    if target == '':
        return [[]]
    
    constructWay = []
    
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            constructWayForRest = allConstruct(suffix, wordBank)
            
            if constructWayForRest != []:
                constructWayForRestLength = len(constructWayForRest)
                
                for i in range(constructWayForRestLength):
                    constructWayForRestAppend = [word]
                    
                    for j in range(len(constructWayForRest[i])):
                        constructWayForRestAppend.append(constructWayForRest[i][j])
                    
                    constructWay.append(constructWayForRestAppend)
    
    return constructWay

""" Memoization """

def allConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    
    if target == '':
        return [[]]
    
    constructWay = []
    
    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            constructWayForRest = allConstruct(suffix, wordBank, memo)
            
            if constructWayForRest != []:
                constructWayForRestLength = len(constructWayForRest)
                
                for i in range(constructWayForRestLength):
                    constructWayForRestAppend = [word]
                    
                    for j in range(len(constructWayForRest[i])):
                        constructWayForRestAppend.append(constructWayForRest[i][j])
                    
                    constructWay.append(constructWayForRestAppend)
    
    memo[target] = constructWay
    return constructWay


"""
allConstruct lecture example
"""

def allConstruct(target, wordBank):
    if target == '':
        return [[]]
    
    result = []

    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            suffixWays = allConstruct(suffix, wordBank)
            # targetWays = [[word] + i for i in suffixWays]
            targetWays = list(map(lambda way: [word] + way, suffixWays))
            [result.append(i) for i in targetWays]
    
    return result

""" Memoization """

def allConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    
    if target == '':
        return [[]]
    
    result = []

    for word in wordBank:
        wordLength = len(word)
        if target[:wordLength] == word:
            suffix = target[wordLength:]
            suffixWays = allConstruct(suffix, wordBank, memo)
            # targetWays = [[word] + i for i in suffixWays]
            targetWays = list(map(lambda way: [word] + way, suffixWays))
            [result.append(i) for i in targetWays]
    
    memo[target] = result
    return result


print(str(allConstruct("abana", ["ab", "a", "an", "na", "abcd"])))
print(str(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])))
print(str(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd","c"])))
print(str(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(str(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])))
print(str(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))



"""
SECTION TABULATION
"""


"""
Fibonacci own example
"""

def fib(n):
    
    if n == 0 or n == 1:
        return n
    
    fibTable = [0] * (n+1)
    fibTable[1] = 1
    
    for i in range(n):
        if i == n-1:
            return fibTable[n] + fibTable[i]
        
        fibTable[i+1] += fibTable[i]
        fibTable[i+2] += fibTable[i]

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


"""
Grid traveller own example
"""

def gridTraveller(n, m):
    if n == 0 or m == 0:
        return 0
    
    sub_table = [0] * (n+1)
    table = list(map(lambda x: [x] * (m+1), sub_table))
    
    table[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
                
            table[i][j] = table[i][j-1] + table[i-1][j]
    
    return table[n][m]


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

"""
Can Sum own example
"""

def canSum(targetSum, numbers):
    table = [False] * (targetSum + 1)
    
    table[0] = True
    
    for i in range(targetSum):
        for j in numbers:
            if table[i]:
                if i + j <= targetSum:
                    table[i + j] = True
    
    return table[targetSum]



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


"""
HowSum own example
"""

def howSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    
    table[0] = []
    
    for i in range(targetSum):
        for num in numbers:
            if table[i] != None:
                if i + num <= targetSum:
                    table[i + num] = table[i] + [num]
    
    return table[targetSum]


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




"""
Best Sum own example
"""

def bestSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    
    table[0] = []
    
    for i in range(targetSum):
        if table[i] != None:
            for num in numbers:
                if i + num <= targetSum:
                    interim_table = table[i].copy()
                    interim_table.append(num)
                    
                    if table[i + num] == None:
                        table[i + num] = interim_table
                    
                    current_value_length = len(interim_table)
                    
                    if current_value_length < len(table[i + num]):
                        table[i + num] = interim_table
    
    return table[targetSum]


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



"""
canConstruct own example
"""

def canConstruct(target, wordBank):
    target_length = len(target)
    table = [False] * (target_length + 1)
    
    table[0] = True
    
    for i in range(target_length):
        if table[i]:
            for word in wordBank:
                if word == target[i:len(word) + i] and i + len(word) <= target_length:
                    table[i + len(word)] = True
    
    return table[target_length]


"""
canConstruct lecture example
"""

def canConstruct(target, wordBank):
    table = [False] * (len(target) + 1)
    table[0] = True
    
    for i in range(len(target)):
        if table[i]:
            for word in wordBank:
                if word == target[i:len(word) + i]:
                    table[i + len(word)] = True
    
    return table[len(target)]

print(str(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])))
print(str(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(str(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])))
print(str(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))



"""
countConstruct own example
"""

def countConstruct(target, wordBank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    
    for i in range(len(target)):
        if table[i] >= 1:
            for word in wordBank:
                if word == target[i:len(word) + i]:
                    table[i + len(word)] += table[i]
                    
    return table[len(target)]


"""
countConstruct lecture example
"""

def countConstruct(target, wordBank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    
    for i in range(len(target)):
        for word in wordBank:
            if word == target[i:len(word) + i]:
                table[i + len(word)] += table[i]
    
    return table[len(target)]

print(str(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])))
print(str(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(str(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])))
print(str(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))



"""
allConstruct own example
"""

def allConstruct(target, wordBank):
    sub_table = [0] * (len(target) + 1)
    table = list(map(lambda x: [], sub_table))
    table[0] += [[]]
    
    for i in range(len(target)):
        if table[i] != []:
            for word in wordBank:
                if word == target[i:len(word) + i]:
                    table[i + len(word)] = table[i + len(word)] + [x + [word] for x in table[i]]
                    
    return table[len(target)]

"""
allConstruct lecture example
"""


def allConstruct(target, wordBank):
    sub_table = [0] * (len(target) + 1)
    table = list(map(lambda x: [], sub_table))
    table[0] += [[]]
    
    for i in range(len(target)):
        if table[i] != []:
            for word in wordBank:
                if word == target[i:len(word) + i]:
                    newCombinations = list(map(lambda x: x + [word], table[i]))
                    table[i + len(word)] = table[i + len(word)] + newCombinations
                    
    return table[len(target)]

print(str(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])))
print(str(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(str(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])))
print(str(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))

"""
countConstruct recursion lecture example
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

"""
countConstruct memoization lecture example 
"""

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
"""
allConstruct recursion lecture example
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

"""
allConstruct memoization lecture example
"""

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
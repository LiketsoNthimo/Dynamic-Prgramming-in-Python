"""
canConstruct recursion lecture adaptation example
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


"""
canConstruct memoization lecture adaptation example
"""

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
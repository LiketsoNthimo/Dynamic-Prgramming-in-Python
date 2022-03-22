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
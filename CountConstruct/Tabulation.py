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
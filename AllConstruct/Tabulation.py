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
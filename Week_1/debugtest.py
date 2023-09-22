

def levenshtein(a,b):
    print(a, b)
    changes = 0
    if len(a) >= len(b):
        pick = a
        other = b
    else: 
        pick = b
        other = a
    for i in range(len(other)):
        if other[i] == pick[i]:
            pass
        elif other[i] not in pick:
            changes +=1

    for l in pick:
        if l not in other:
            changes +=1
    return changes


print(levenshtein("asdfara","adagathsr"))
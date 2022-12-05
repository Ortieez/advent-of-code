import string

LOWERCASE = list(string.ascii_lowercase)
UPPERCASE = list(string.ascii_uppercase)

def goThroughAlphabet(toCheckFor, upper) -> int:
    if upper:
        return UPPERCASE.index(toCheckFor) + 27
    else:
        return LOWERCASE.index(toCheckFor) + 1

score = 0
values = open("prodSet.txt", "r").read()
values = values.split("\n")

for value in values:
    tmp = list(value)
    tmp_length = len(tmp)

    firstComp = []
    secondComp = []
    check = 0
    for char in tmp:     
        if (check < tmp_length / 2):
            firstComp.append(char)
        elif(check < tmp_length):
            secondComp.append(char)

        check+=1

    aSet = set(firstComp)
    bSet = set(secondComp)   

    other = aSet.intersection(bSet)

    currentVal = ""
    for val in other:
        currentVal = val
    if(currentVal.islower()):
        score+=goThroughAlphabet(currentVal, False)
    else:
        score+=goThroughAlphabet(currentVal, True)

print(score)
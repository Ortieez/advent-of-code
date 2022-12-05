import string

LOWERCASE = list(string.ascii_lowercase)
UPPERCASE = list(string.ascii_uppercase)

def goThroughAlphabet(toCheckFor, upper) -> int:
    if upper:
        return UPPERCASE.index(toCheckFor) + 27
    else:
        return LOWERCASE.index(toCheckFor) + 1

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


score = 0
values = open("prodSet.txt", "r").read()
values = values.split("\n")

elves = chunks(values, 3)

for jednaTrojice in elves:
    aSet = set(jednaTrojice[0])
    bSet = set(jednaTrojice[1])   
    cSet = set(jednaTrojice[2])
    intersection = aSet & bSet & cSet

    for val in intersection:
        currentVal = val
        if(currentVal.islower()):
            score+=goThroughAlphabet(currentVal, False)
        else:
            score+=goThroughAlphabet(currentVal, True)


print(score)
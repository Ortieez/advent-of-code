ROUNDCONFIG = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "win": 6,
    "tie": 3,
}

SUBSTITUTION = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

score = 0

values = open("prodSet.txt", "r").read()
values = values.split("\n")

for rpsRound in values:
    temp = rpsRound.split(" ")
    temp[0] = SUBSTITUTION[temp[0]]

    score += ROUNDCONFIG[temp[1]]

    if(temp[0] == temp[1]):
        score += ROUNDCONFIG["tie"]

    if(temp[1] == "X" and temp[0] == "Z"):
        score += ROUNDCONFIG["win"]

    if(temp[1] == "Y" and temp[0] == "X"):
        score += ROUNDCONFIG["win"]

    if(temp[1] == "Z" and temp[0] == "Y"):
        score += ROUNDCONFIG["win"]

print(score)
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

SUBSTITUTION_PREDICTION = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

score = 0

values = open("prodSet.txt", "r").read()
values = values.split("\n")

for rpsRound in values:
    temp = rpsRound.split(" ")
    temp[0] = SUBSTITUTION[temp[0]]

    if (temp[1] == "X"):
        if (temp[0] == "X"):
            score += ROUNDCONFIG["Z"]

        if (temp[0] == "Y"):
            score += ROUNDCONFIG["X"]

        if (temp[0] == "Z"):
            score += ROUNDCONFIG["Y"]

    if (temp[1] == "Y"):
        score+= ROUNDCONFIG[temp[0]]
        score+= ROUNDCONFIG["tie"]

    if (temp[1] == "Z"):
        score+=ROUNDCONFIG["win"]
        if (temp[0] == "X"):
            score += ROUNDCONFIG["Y"]

        if (temp[0] == "Y"):
            score += ROUNDCONFIG["Z"]

        if (temp[0] == "Z"):
            score += ROUNDCONFIG["X"]
print(score)
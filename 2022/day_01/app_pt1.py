values = open("prodSet.txt", "r").read()
values = values.split("\n")
elfs = []
temp = 0
for val in values: 
    if (val == ''): 
        elfs.append(temp)
        temp = 0
    else: 
        temp += int(val)

maxNum = 0
maxNumPos = 0
for index, elf in enumerate(elfs):
    if elf > maxNum:
        maxNum = elf
        maxNumPos = index

print(elfs[maxNumPos])

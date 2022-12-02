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

elfs.sort(reverse=True)

count = elfs[0] + elfs[1] + elfs[2]
print(elfs)
print(count)
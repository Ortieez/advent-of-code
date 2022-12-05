values = open("prodSet.txt", "r").read()
values = values.split("\n")

fullE01 = []
fullE02 = []

counter = 0


for pair in values:
    e01 = pair.split(",")[0].split("-")
    e01 = [int(e01[0]), int(e01[1])]
    e02 = pair.split(",")[1].split("-")
    e02 = [int(e02[0]), int(e02[1])]
    
    # print(e01[0], e01[1])
    for i in range(e01[0], e01[1] + 1, 1):
        fullE01.append(i)

    # print(e02[0], e02[1])
    for i in range(e02[0], e02[1] + 1, 1):
        fullE02.append(i)

    fullE01 = set(fullE01)
    fullE02 = set(fullE02)

    

    if len(fullE01) < len(fullE02):
        fullE02, fullE01 = fullE01, fullE02

    test = fullE02.issubset(fullE01)

    print(e01, e02, '\n', fullE01, fullE02,'\n',  test , '\n-----------------------', )


    if test:
        counter+=1

    fullE01 = []
    fullE02 = []  

print(counter)
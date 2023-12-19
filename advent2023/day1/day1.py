import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r").read()
total = 0
test = ["thistwo1isnot45anumber", "non4point"]
numstrings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for x in f:
    firstnum = -1
    lastnum = -1
    for i in range(len(x)):
        y = x[i]
        if y.isdigit():
            if firstnum == -1:
                firstnum = y
            else:
                lastnum = y
        else:
            for key in numstrings:
                if x[i:].startswith(key):
                    if firstnum == -1:
                        firstnum = numstrings[key]
                    else:
                        lastnum = numstrings[key]

    if lastnum == -1:
        lastnum = firstnum

    res = int(firstnum + lastnum)
    total += res

print(total)

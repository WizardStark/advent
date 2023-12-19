import os, sys

test = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]

input = open(os.path.join(sys.path[0], "input.txt"), "r").read()


def notSum(arr):
    if len(arr) == 1:
        return arr[0]
    arr[-1] = arr[-2] - arr.pop()
    return notSum(arr)


def eval(line):
    if all(x == 0 for x in line[-1]):
        return sum(x[-1] for x in line), notSum([x[0] for x in line])
    line.append([line[-1][i + 1] - line[-1][i] for i in range(len(line[-1]) - 1)])
    return eval(line)


def sol(input):
    vals = [x.split() for x in input.splitlines()]
    total = 0
    prevTotal = 0
    for line in vals:
        line = list(map(int, line))
        res = eval([line])
        total += res[0]
        prevTotal += res[1]
    print(total, prevTotal)


sol(input)

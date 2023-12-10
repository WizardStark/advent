from math import ceil, floor, sqrt

test = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]

input = [
    "Time:        34     90     89     86",
    "Distance:   204   1713   1210   1780",
]


def solve(t, d):
    low = ceil(0.5 * t + sqrt(t * t - 4 * d) / 2)
    high = floor(0.5 * t - sqrt(t * t - 4 * d) / 2)

    return abs(high - low + 1)


def part1(input):
    t = list(map(int, input[0].split(":")[1].split()))
    d = list(map(int, input[1].split(":")[1].split()))
    total = 1
    for i, time in enumerate(t):
        ways = solve(time, d[i])
        total *= ways

    print(total)

    t = int(input[0].split(":")[1].replace(" ", ""))
    d = int(input[1].split(":")[1].replace(" ", ""))

    total = solve(t, d)

    print(total)


part1(input)

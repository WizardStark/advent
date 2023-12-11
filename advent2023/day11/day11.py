import os, sys, time

f = open(os.path.join(sys.path[0], "input.txt"), "r").read()

test = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


def parse(input):
    return list(map(list, input.splitlines()))


def expand(img, exp_fact):
    i = 0
    while i < len(img[0]):
        col = [x[i] for x in img]
        if not "#" in col:
            for x in range(len(img)):
                img[x][i] = exp_fact
        i += 1
    i = 0
    while i < len(img):
        if not "#" in img[i]:
            for x in range(len(img[i])):
                img[i][x] = exp_fact
        i += 1
    return img


def sol(input, exp_fact):
    img = expand(parse(input), exp_fact)
    stars = []
    total = 0
    y_pos = 0
    for i in range(len(img)):
        x_pos = 0
        for j in range(len(img[0])):
            if img[i][j] == "#":
                total += sum([abs(x[0] - x_pos) + abs(x[1] - y_pos) for x in stars])
                stars.append((x_pos, y_pos))
            if img[i][j] == exp_fact:
                x_pos += exp_fact
            else:
                x_pos += 1

        if all(x == exp_fact for x in img[i]):
            y_pos += exp_fact
        else:
            y_pos += 1

    print(total)


start = time.time()
# sol(f, 2)
sol(f, 1000000)
end = time.time()
print("Time:", end - start)

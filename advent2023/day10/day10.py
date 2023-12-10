import time
from math import ceil

f = open("day10/input.txt", "r").read()


test = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

test2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""


# [left, right, up, down]
pipes = {
    "|": [0, 0, 1, 1],
    "-": [1, 1, 0, 0],
    "L": [0, 1, 1, 0],
    "J": [1, 0, 1, 0],
    "7": [1, 0, 0, 1],
    "F": [0, 1, 0, 1],
    ".": [0, 0, 0, 0],
}


def sol(input):
    pipe_map = input.split("\n")[:-1]
    inside = [[0] * len(pipe_map[0]) for _ in range(len(pipe_map))]
    just_pipes = [["O"] * len(pipe_map[0]) for _ in range(len(pipe_map))]
    x, y = 0, 0
    for i, row in enumerate(pipe_map):
        if (pos := row.find("S")) != -1:
            x, y = pos, i
    connected = [
        0 if x == 0 else pipes[pipe_map[y][x - 1]][1],
        0 if x + 1 == len(pipe_map[x]) else pipes[pipe_map[y][x + 1]][0],
        0 if y == 0 else pipes[pipe_map[y - 1][x]][3],
        0 if y + 1 == len(pipe_map) else pipes[pipe_map[y + 1][x]][2],
    ]
    prev_move = [0, 0, 0, 0]
    for i in range(len(connected)):
        if connected[i] == 1:
            prev_move[i] = 1
            break

    moves = 0
    current_tile = list(pipes.keys())[list(pipes.values()).index(connected)]
    while current_tile != "S":
        just_pipes[y][x] = current_tile
        x += prev_move[1] - prev_move[0]
        y += prev_move[3] - prev_move[2]
        current_tile = pipe_map[y][x]
        if current_tile == "S":
            break
        prev_move = [
            pipes[current_tile][0] - prev_move[1],
            pipes[current_tile][1] - prev_move[0],
            pipes[current_tile][2] - prev_move[3],
            pipes[current_tile][3] - prev_move[2],
        ]

        moves += 1

    for i, line in enumerate(just_pipes):
        is_inside = False
        has_pc = False
        pc = "-"
        for j, c in enumerate(line):
            if c == "O":
                inside[i][j] = int(is_inside)
                continue
            if c == "F" or c == "J" or c == "L" or c == "7":
                if has_pc:
                    vchange = abs(pipes[c][2] - pipes[pc][2]) + abs(
                        pipes[c][3] - pipes[pc][3]
                    )
                    if vchange != 0:
                        is_inside = not is_inside
                    has_pc = False
                else:
                    has_pc = True
                pc = c
            if c == "|":
                is_inside = not is_inside

    print(ceil(moves / 2))
    print(sum(map(sum, inside)))


# part1(test3)

starttime = time.time()
sol(f)
endtime = time.time()

print("Time:", endtime - starttime)

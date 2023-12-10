test = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def parse(game):
    return (
        game.replace(",", "")
        .replace(";", "")
        .replace(":", "")
        .replace("\n", "")
        .split(" ")
    )


def part1(f):
    total = 0
    limits = {"red": 12, "green": 13, "blue": 14}
    for game in f:
        game = parse(game)

        for j in range(len(game)):
            if game[j] in limits.keys():
                if int(game[j - 1]) > limits[game[j]]:
                    game = "0"
                    break

        if game != "0":
            game = game[1]

        total += int(game)

    print(total)


def part2(f):
    total_power = 0

    for game in f:
        game = parse(game)
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for j in range(len(game)):
            if game[j] in min_cubes.keys():
                if int(game[j - 1]) > min_cubes[game[j]]:
                    min_cubes[game[j]] = int(game[j - 1])
        total_power += min_cubes["red"] * min_cubes["blue"] * min_cubes["green"]

    print(total_power)


f = open("day2/input.txt", "r")
part1(f)

f = open("day2/input.txt", "r")
part2(f)

from enum import Enum


class RPS(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Result(Enum):
    WIN = 0
    LOSE = 1
    DRAW = 2


scores = {
    RPS.ROCK: 1,
    RPS.PAPER: 2,
    RPS.SCISSORS: 3,
    Result.WIN: 6,
    Result.LOSE: 0,
    Result.DRAW: 3,
}


def letter_to_rps(let):
    if let == "A" or let == "X":
        return RPS.ROCK
    elif let == "B" or let == "Y":
        return RPS.PAPER
    elif let == "C" or let == "Z":
        return RPS.SCISSORS


def letter_to_rps_part2(enemy_rps: RPS, let: str):
    if let == "X":  # lose
        return RPS((enemy_rps.value - 1) % 3)
    elif let == "Y":  # draw
        return enemy_rps
    elif let == "Z":  # win
        return RPS((enemy_rps.value + 1) % 3)


def game_result(player: RPS, enemy: RPS):
    if player == enemy:
        return Result.DRAW
    if player.value == (enemy.value + 1) % 3:
        return Result.WIN
    return Result.LOSE


def line_score(line: str):
    if line == "":
        return 0
    parts = line.split(" ")
    enemy = letter_to_rps(parts[0])
    player = letter_to_rps(parts[1])
    return scores[game_result(player, enemy)] + scores[player]


def line_score_2(line: str):
    if line == "":
        return 0
    parts = line.split(" ")
    enemy = letter_to_rps(parts[0])
    player = letter_to_rps_part2(enemy, parts[1])
    return scores[game_result(player, enemy)] + scores[player]


if __name__ == "__main__":
    total = sum([line_score(line) for line in open("input.txt").read().split('\n')])
    print(f"part1 total: {total}")
    total2 = sum([line_score_2(line) for line in open("input.txt").read().split('\n')])
    print(f"part2 total: {total2}")

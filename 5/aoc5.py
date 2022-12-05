def parse_stacks(stacks: str) -> dict[int, list[str]]:
    buckets = {}
    lines = stacks.split("\n")
    num_buckets = int(lines[-1].strip().split(' ')[-1])
    for i in range(1, num_buckets + 1):
        buckets[i] = []
    for line in stacks.split("\n")[:-1]:
        for i in buckets:
            line_idx = 4 * (i - 1) + 1
            if line[line_idx] != " ":
                buckets[i].append(line[line_idx])
    for i in buckets:
        buckets[i].reverse()

    return buckets


def parse_move_line(move: str) -> tuple[int, int, int]:
    bits = move.split(" ")
    return int(bits[1]), int(bits[3]), int(bits[5])


def process_move(buckets: dict[int, list[str]], movenum: int, movefrom: int, moveto: int) -> None:
    for _ in range(movenum):
        buckets[moveto].append(buckets[movefrom].pop())


def process_move_v2(buckets: dict[int, list[str]], movenum: int, movefrom: int, moveto: int) -> None:
    tmp = []
    for _ in range(movenum):
        tmp.append(buckets[movefrom].pop())
    tmp.reverse()
    buckets[moveto].extend(tmp)


def process_moves(
        buckets: dict[int, list[str]], moves: list[str], *, v2: bool = False
) -> dict[int, list[str]]:
    fn = process_move_v2 if v2 else process_move
    for line in moves:
        movenum, movefrom, moveto = parse_move_line(line)
        fn(buckets, movenum, movefrom, moveto)
    return buckets


if __name__ == "__main__":
    import copy

    infile = open("input.txt").read().split("\n\n")

    stacks = infile[0]
    moves = infile[1].split("\n")[:-1]

    buckets1 = parse_stacks(stacks)
    buckets2 = copy.deepcopy(buckets1)  # needed for part 2 since the solution mutates it

    final_buckets = process_moves(buckets1, moves)
    answer = "".join([final_buckets[i][-1] for i in final_buckets])
    print(f"Part 1: {answer}")

    final_buckets2 = process_moves(buckets2, moves, v2=True)
    answer2 = "".join([final_buckets2[i][-1] for i in final_buckets2])
    print(f"Part 2: {answer2}")

def letter_score(letter: str):
    val = ord(letter)
    if val >= ord("a"):
        return val - ord("a") + 1
    return val - ord("A") + 27


def find_char_out_of_place(line: str):
    halflen = len(line) // 2
    lhs_set = set((x for x in line[0:halflen]))
    rhs_set = set((x for x in line[halflen:]))
    shared_letter = (lhs_set & rhs_set).pop()
    return shared_letter


def find_common_in_group(group: tuple[str, str, str]):
    return (set(group[0]) & set(group[1]) & set(group[2])).pop()


if __name__ == "__main__":
    inputdata = open("input.txt").read().split("\n")[0:-1]
    lines = [letter_score(find_char_out_of_place(line)) for line in inputdata]
    print(f"Total sum: {sum(lines)}")

    groups = [
        (inputdata[x], inputdata[x + 1], inputdata[x + 2])
        for x in range(0, len(inputdata), 3)
    ]
    p2vals = [letter_score(find_common_in_group(g)) for g in groups]
    print(f"Part2 sum: {sum(p2vals)}")

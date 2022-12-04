def pairs_overlap(line: list[list[int]]):
    one_is_contained = ((line[0][0] <= line[1][0]) & (line[0][1] >= line[1][1])) | (
        (line[0][0] >= line[1][0]) & (line[0][1] <= line[1][1])
    )
    return one_is_contained


if __name__ == "__main__":
    lines = open("input.txt").readlines()
    pairs = [
        [[int(x) for x in (pair.split("-"))] for pair in line.strip().split(",")]
        for line in lines
    ]
    cont = [pairs_overlap(pair) for pair in pairs]
    num = len([x for x in cont if x is True])
    print(f"number of overlaps: {num}")

def pairs_wholly_overlap(line: list[list[int]]):
    one_is_contained = ((line[0][0] <= line[1][0]) & (line[0][1] >= line[1][1])) | (
        (line[0][0] >= line[1][0]) & (line[0][1] <= line[1][1])
    )
    return one_is_contained


def pairs_partially_overlap(line: list[list[int]]):
    low_overlap = (
        # lhs overlaps at low end of rhs
        ((line[0][0] <= line[1][0]) & (line[0][1] >= line[1][0]))
        # rhs overlaps low end of lhs
        | ((line[0][0] >= line[1][0]) & (line[0][0] <= line[1][1]))
    )
    high_overlap = (
        # lhs overlaps high end of rhs
        ((line[0][0] <= line[1][1]) & (line[0][1] >= line[1][1]))
        # rhs overlaps high end of lhs
        | ((line[0][1] >= line[1][0]) & (line[0][1] <= line[1][1]))
    )
    return low_overlap | high_overlap | pairs_wholly_overlap(line)


if __name__ == "__main__":
    lines = open("input.txt").readlines()
    pairs = [
        [[int(x) for x in (pair.split("-"))] for pair in line.strip().split(",")]
        for line in lines
    ]
    contained = [pairs_wholly_overlap(pair) for pair in pairs]
    num = len([x for x in contained if x is True])
    print(f"number of overlaps: {num}")

    partial = [pairs_partially_overlap(pair) for pair in pairs]
    numv2 = len([x for x in partial if x is True])
    print(f"Number of partial overlaps: {numv2}")

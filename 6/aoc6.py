def allunique(fourchars: str):
    return (
        fourchars[3] not in fourchars[0:3]
        and fourchars[2] not in fourchars[0:2]
        and fourchars[1] != fourchars[0]
    )


def allunique_n(chars: str, n: int):
    return all((chars[k] not in chars[0:k] for k in range(n - 1, 0, -1)))


def find_first_four_different(msg: str) -> int:
    """
    Returns the index one past the group of 4 different characters
    """
    for i in range(3, len(msg)):
        last4 = msg[i - 3 : i + 1]
        if allunique(last4):
            return i + 1
    raise "no index found! :("


def find_first_n_different(msg: str, n: int) -> int:
    """
    Returns the index one past the group of 4 different characters
    """
    for i in range(n - 1, len(msg)):
        lastn = msg[i - n + 1 : i + 1]
        if allunique_n(lastn, n):
            return i + 1
    raise "no index found! :("


# fmt: off
# @formatter:off
def codegolf_solution():
    """
    A 'fun' solution rewriting the whole find-first-n function as a comprehension
    """

    def f(m, n):
        return next(i+1 for i in range(n-1, len(m)) if (all((m[k] not in m[i-n+1:k] for k in range(i,i-n,-1)))))
    m=open("input.txt").read()
    print(f"1: {f(m,4)}, 2:{f(m,14)}")

# @formatter:on
# fmt: on


def main() -> None:
    import sys

    infile = "input.txt"
    if len(sys.argv) == 2:
        infile = sys.argv[1]
    message = open(infile).read()
    idx = find_first_four_different(message)
    print(f"Part1: first marker after character {idx}")
    idx2 = find_first_n_different(message, 14)
    print(f"Part2: first marker after character {idx2}")


if __name__ == "__main__":
    main()

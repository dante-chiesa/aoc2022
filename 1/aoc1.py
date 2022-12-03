import heapq

INPUT_FILE = "input.txt"

# just for REPL
TESTDATA = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def read_calories_to_arr(infile):
    with open(infile, "r") as f:
        return [x.strip() for x in f.readlines()]


def calories_per_elf(calorie_array):
    curelf = 0
    elfsums = {curelf: 0}

    for line in calorie_array:
        if line != "":
            val = int(line)
            elfsums[curelf] += val
        else:
            curelf = curelf + 1
            elfsums[curelf] = 0
    return elfsums


def highest_calories(per_elf):
    max_val = 0
    max_idx = -1
    for idx in per_elf:
        if per_elf[idx] > max_val:
            max_val = per_elf[idx]
            max_idx = idx
    return max_idx


def highest_three_calories(per_elf):
    threshold = 0
    # we will keep this sorted in reverse order so we can pop the last elem to remove the min
    top3 = []

    def getcals(pair):
        (_, cals) = pair
        return cals

    def push_top3(idx, val):
        nonlocal top3, threshold
        top3.append((idx, val))
        top3 = sorted(top3, key=getcals, reverse=True)
        if len(top3) > 3:
            top3.pop()
            threshold = top3[2][1]

    for idx in per_elf:
        calories = per_elf[idx]
        if calories > threshold:
            push_top3(idx, calories)

    return top3


def calories_per_elf_v2(calorie_array):
    # improved version uses a list instead of a dict as
    # we actually never cared about which elf was which and don't need the indices
    cals = [0]
    cur = 0
    for line in calorie_array:
        if line != "":
            cals[cur] += int(line)
        else:
            cur = cur + 1
            cals.append(0)
    return cals


def highest_three_calories_v2(cals_list):
    # improved version uses the heap functions from standard library
    # hey, data structures are cool!
    heapq.heapify(cals_list)
    return heapq.nlargest(3, cals_list)


if __name__ == "__main__":
    arr = read_calories_to_arr(INPUT_FILE)
    perelf = calories_per_elf(arr)
    max_elf = highest_calories(perelf)
    print(f"highest calores: elf #{max_elf} at {perelf[max_elf]}")

    top3 = highest_three_calories(perelf)
    print(f"top 3: {top3}, sum: {sum([x[1] for x in top3])}")

    perelf_v2 = calories_per_elf_v2(arr)
    top3_v2 = highest_three_calories_v2(perelf_v2)
    print(f"top 3 (alternate method): {top3_v2}, sum: {sum(top3_v2)}")

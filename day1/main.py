
from collections import defaultdict


if __name__ == "__main__":

    fn = "input.txt"

    with open(fn, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    lines = [[int(n) for n in line.split("   ")] for line in lines]

    left, right = list(zip(*lines))
    left = list(left)
    right = list(right)

    left.sort()
    right.sort()

    diff = [abs(left[i] - right[i]) for i in range(len(left))]

    print(sum(diff))

    right_count = defaultdict(int)
    for r in right:
        right_count[r] += 1


    cumulative = 0
    for l in left:
        cumulative += l * right_count[l]

    print(cumulative)

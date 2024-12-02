# super clean pythonic solution
from collections import Counter

if __name__ == "__main__":
    lines = [list(map(int, line.split())) for line in open("input.txt")]
    left, right = map(sorted, list(zip(*lines)))

    # part 1
    print(sum(abs(l - r) for l, r in zip(left, right)))

    # part 2
    freq = Counter(right)
    print(sum(l * freq[l] for l in left))

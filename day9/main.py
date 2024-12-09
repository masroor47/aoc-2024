from collections import defaultdict, Counter
from tqdm import tqdm

def checksum(line):
    res = 0
    for i, c in enumerate(line):
        if c == '.': continue
        n = int(c)
        res += i * n
    return res

def checksum_new(memory: list):
    res = 0
    pos = 0
    for i, m in enumerate(memory):
        if isinstance(m, int):
            pos += m
            continue
        else:
            for j in range(m[1]):
                res += m[0] * pos
                pos += 1
    return res

def part1(fn):
    lines = [line.strip() for line in open(fn)]
    line = lines[0]

    memory = []
    empty = False
    id = 0
    for i, c in enumerate(line):
        if empty:
            empty = False
            for _ in range(int(c)):
                memory.append('.')
        else:
            empty = True
            for _ in range(int(c)):
                memory.append(str(id))
            id += 1

    # print("".join(memory))

    l = 0
    r = len(memory) - 1
    while True:
        if memory[r] == '.':
            r -= 1
        else:
            break
    
    while l < r:
        if memory[l] == '.' and memory[r] != '.':
            memory[l], memory[r] = memory[r], memory[l]
            l += 1
            r -= 1
        elif memory[l] != '.':
            l += 1
        elif memory[r] == '.':
            r -= 1

    return checksum(memory)

def convert_to_str(memory):
    res = []
    for m in memory:
        if isinstance(m, int):
            res.append('.' * m)
        else:
            res.append(str(m[0])*m[1])
    return "".join(res)


def part2(fn):
    line = open(fn).read().strip()

    memory = []
    empty = False
    id = 0
    for i, c in enumerate(line):
        if empty:
            memory.append(int(c))
            empty = False
        else:
            memory.append((id, int(c), False))
            empty = True
            id += 1

    # seeing this made me realize ids are not one-digit...
    # with open('memory.txt', 'w') as f:
    #     f.write(convert_to_str(memory))
    
    r = len(memory) - 1
    # now l and r point to regions in memory, not individual blocks
    with tqdm(total=len(memory)-1, desc="Processing memory") as pbar:
        while r > 0:
            right = memory[r]
            if isinstance(right, int):
                r -= 1
                pbar.update(1)
                continue

            if right[2]:
                r -= 1
                pbar.update(1)
                continue

            for l in range(r):
                left = memory[l]
                if isinstance(left, int) and isinstance(right, tuple):
                    if left >= right[1]:
                        memory[l] = (right[0], right[1], True)
                        memory[r] = right[1]
                        if left - right[1] > 0:
                            memory.insert(l+1, left - right[1])
                            r += 1
                        break
            r -= 1
            pbar.update(1)

    return checksum_new(memory)

if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))
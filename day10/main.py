from collections import defaultdict, Counter


dRow = [0, 1, 0, -1]
dCol = [-1, 0, 1, 0]

def is_valid(r, c, lines, visited):
    # print(len(lines), len(lines[0]))
    if r < 0 or c < 0 or r >= len(lines) or c >= len(lines[0]):
        return False
    if (r, c) in visited:
        return False
    return True

def count_reachable_nines(lines, start_r, start_c, unique=True):
    dRow = [-1, 0, 1, 0]  # up, right, down, left
    dCol = [0, 1, 0, -1]

    r = start_r
    c = start_c

    stack = [(r, c, -1, set())]
    res = 0

    nines = set()
    
    while stack:
        r, c, prev_height, visited = stack.pop()
        current_height = lines[r][c]
        
        # Check if this is a valid next step
        if prev_height != -1 and current_height != prev_height + 1:
            continue

        # print(f"{r}, {c} is a valid next step, with height {current_height}")
            
        # Create a new visited set for this path
        new_visited = visited | {(r, c)}
        
        # Found a valid 9
        if current_height == 9:
            if unique:
                if (r, c) not in nines:
                    nines.add((r, c))
            else:
                res += 1
            continue
            
        for i in range(4):
            new_r = r + dRow[i]
            new_c = c + dCol[i]
            
            if is_valid(new_r, new_c, lines, visited):  # Use current path's visited set
                stack.append((new_r, new_c, current_height, new_visited))

    if unique:
        return len(nines)
    return res

def part1(fn):
    lines = [list(map(int, list(line.strip()))) for line in open(fn)]

    starting = set()
    for r, line in enumerate(lines):
        for c, val in enumerate(line):
            if val == 0:
                starting.add((r, c))

    print(f"There are {len(starting)} starting points")

    total = 0
    for start_r, start_c in starting:
        total += count_reachable_nines(lines, start_r, start_c, unique=True)

    return total



def part2(fn):
    lines = [list(map(int, list(line.strip()))) for line in open(fn)]

    starting = set()
    for r, line in enumerate(lines):
        for c, val in enumerate(line):
            if val == 0:
                starting.add((r, c))

    total = 0
    for start_r, start_c in starting:
        total += count_reachable_nines(lines, start_r, start_c, unique=False)
    return total

if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))
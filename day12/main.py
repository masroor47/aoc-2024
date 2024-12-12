


def calc_cost(r, c, lines, visited):
    print(f"Calculating cost for {r}, {c}, {lines[r][c]}")
    stack = [(r, c)]
    area = 0
    perimiter = 0
    while stack:
        r, c = stack.pop()
        curr_char = lines[r][c]

        if (r, c) in visited:
            continue
        visited.add((r, c))
        area += 1

        if r > 0 and lines[r-1][c] == curr_char:
            stack.append((r-1, c))
        else:
            perimiter += 1

        if r < len(lines) - 1 and lines[r+1][c] == curr_char:
            stack.append((r+1, c))
        else:
            perimiter += 1
        
        if c > 0 and lines[r][c-1] == curr_char:
            stack.append((r, c-1))
        else:
            perimiter += 1
        
        if c < len(lines[0]) - 1 and lines[r][c+1] == curr_char:
            stack.append((r, c+1))
        else:
            perimiter += 1

    print(f"Area: {area}, Perimiter: {perimiter}")
    return area * perimiter
    

def part1(fn):
    lines = [line.strip() for line in open(fn)]

    visited = set()
    total = 0
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if (r, c) in visited:
                continue
                
            total += calc_cost(r, c, lines, visited)

    return total

def calc_area_and_sides(r, c, lines, visited):
    print(f"Calculating area and sides for {r}, {c}, {lines[r][c]}")
    stack = [(r, c, [])]
    stack_set = set([(r, c)])
    area = 0
    num_sides = 0

    while stack:
        r, c, exposed_sides = stack.pop(0)
        curr_char = lines[r][c]

        if (r, c) in visited:
            continue
        visited.add((r, c))
        area += 1
        next_exposed_sides = []

        if r == 0 or (r > 0 and lines[r-1][c] != curr_char):
            next_exposed_sides.append("top")
            if 'top' not in exposed_sides:
                num_sides += 1

        if r == len(lines) - 1 or (r < len(lines) - 1 and lines[r+1][c] != curr_char):
            next_exposed_sides.append("bottom")
            if 'bottom' not in exposed_sides:
                num_sides += 1

        if c == 0 or (c > 0 and lines[r][c-1] != curr_char):
            next_exposed_sides.append("left")
            if 'left' not in exposed_sides:
                num_sides += 1

        if c == len(lines[0]) - 1 or (c < len(lines[0]) - 1 and lines[r][c+1] != curr_char):
            next_exposed_sides.append("right")
            if 'right' not in exposed_sides:
                num_sides += 1

        print(f"({r}, {c}) - {curr_char}: {exposed_sides} -> {next_exposed_sides}, num_sides: {num_sides}")

        for next_r, next_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if next_r >= 0 and next_r < len(lines) and next_c >= 0 and next_c < len(lines[0]) and lines[next_r][next_c] == curr_char:
                if (next_r, next_c) not in visited:
                    if (next_r, next_c) not in stack_set:
                        stack_set.add((next_r, next_c))
                        stack.append((next_r, next_c, next_exposed_sides))
                        # print('scheduling', next_r, next_c, next_exposed_sides, end=' ')
                    else:
                    # find the cell in the stack and update its exposed sides
                        for i, (r_, c_, _) in enumerate(stack):
                            if r_ == next_r and c_ == next_c:
                                old_exposed_sides = stack[i][2]
                                stack[i] = (r_, c_, list(set(old_exposed_sides + next_exposed_sides)))
                                print('updating', next_r, next_c, next_exposed_sides, end=' ')
            print()

    print(f"Area: {area}, Num Sides: {num_sides}")
    return area * num_sides

def part2(fn):
    lines = [line.strip() for line in open(fn)]

    visited = set()
    total = 0
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if (r, c) in visited:
                continue
                
            total += calc_area_and_sides(r, c, lines, visited)
    return total


if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))
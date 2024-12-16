

def print_grid(grid, r, c):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if i == r and j == c:
                print('@', end='')
            else:
                print(cell, end='')
        print()

def check_can_move(grid, r, c, dir):
    next_r, next_c = r + dir[0], c + dir[1]
    if grid[next_r][next_c] == '#':
        # print('initial wall')
        return False
    
    while grid[next_r][next_c] == 'O':
        next_r, next_c = next_r + dir[0], next_c + dir[1]
    
    # next_r, next_c = next_r + dir[0], next_c + dir[1]
    # print(f"next_r: {next_r}, next_c: {next_c}")
    if grid[next_r][next_c] == '#':
        # print('final wall')
        return False
    return True

def make_move(grid, r, c, dir):
    grid[r][c] = '.'
    next_r, next_c = r + dir[0], c + dir[1]
    while grid[next_r][next_c] == 'O':
        next_r, next_c = next_r + dir[0], next_c + dir[1]
    grid[next_r][next_c] = 'O'

    return grid

str_to_dir = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def part1(fn):
    lines = [line.strip() for line in open(fn)]
    divider = lines.index('')
    grid = [list(line) for line in lines[:divider]]
    moves = "".join(lines[divider+1:])

    for r, row in enumerate(grid):
        print(row)
        for c, cell in enumerate(row):
            if cell == '@':
                start = (r, c)
                break
    print(start)
    print(moves)
    print()

    r, c = start
    for move in moves:
        dir = str_to_dir[move]
        # print(move)
        if check_can_move(grid, r, c, dir):
            grid = make_move(grid, r, c, dir)
            r, c = r + dir[0], c + dir[1]
        # print_grid(grid, r, c)

        # print(f"r: {r}, c: {c}")

    gps_score = 0
    grid[r][c] = '.'
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'O':
                # print(r, c)
                gps_score += r*100 + c

    return gps_score



def widen_grid(grid):
    # create deep copy of grid
    new_grid = []
    for r, row in enumerate(grid):
        new_row = []
        for c, cell in enumerate(row):
            if cell == '#':
                new_row.extend(['#', '#'])
            elif cell == '.':
                new_row.extend(['.', '.'])
            elif cell == 'O':
                new_row.extend(['[', ']'])
            elif cell == '@':
                new_row.extend(['@', '.'])
                col = new_row.index('@')

        new_grid.append(new_row)

    return new_grid, col

def check_can_move2(grid, r, c, dir):
    next_r, next_c = r + dir[0], c + dir[1]
    if grid[next_r][next_c] == '#':
        return False
    
    while grid[next_r][next_c] == '[' or grid[next_r][next_c] == ']':
        next_r, next_c = next_r + dir[0], next_c + dir[1]
    
    if grid[next_r][next_c] == '#':
        return False
    return True

def make_move2(grid, r, c, dir):
    pass

def part2(fn):
    lines = [line.strip() for line in open(fn)]
    divider = lines.index('')
    grid = [list(line) for line in lines[:divider]]
    moves = "".join(lines[divider+1:])

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@':
                start = (r, c)
                break
    print(start)
    print(moves)
    print_grid(grid, start[0], start[1])
    grid, c = widen_grid(grid)
    r = start[0]
    print('after widening:')
    print_grid(grid, r, c)
    print()


if __name__ == '__main__':
    # print(part1('input.txt'))
    print(part2('test2.txt'))
from collections import defaultdict, Counter


def check_can_reach(r, c, r_, c_, lines):
    if r == r_:
        if c < c_:
            for i in range(c, c_):
                if lines[r][i] == '#':
                    return False
        else:
            for i in range(c_, c):
                if lines[r][i] == '#':
                    return False
    else:
        if r < r_:
            for i in range(r, r_):
                if lines[i][c] == '#':
                    return False
        else:
            for i in range(r_, r):
                if lines[i][c] == '#':
                    return False
    return True
    

if __name__ == '__main__':
    lines = [line.strip() for line in open("input.txt")]


    # search for guard
    row = 0
    for r, line in enumerate(lines):
        col = line.find('^')

        if col != -1:
            row = r
            break

    print(f"guard at {row}, {col}")

    starting_row = row
    starting_col = col

    # set direction up
    direction = (-1, 0)

    count = 1
    while 0 <= row < len(lines) and 0 <= col < len(lines[row]):
        # print(f"guard at {row}, {col}, pointing {direction}")
        if direction == (-1, 0):
            # if leaving the grid, break
            if row + direction[0] < 0:
                break
            if lines[row + direction[0]][col + direction[1]] != '#':
                if lines[row + direction[0]][col + direction[1]] != 'X':
                    count += 1
                lines[row] = lines[row][:col] + 'X' + lines[row][col + 1:]
                row += direction[0]
            elif lines[row + direction[0]][col + direction[1]] == '#':
                direction = (0, 1)
                # print(f"changing direction, count is {count}")
        elif direction == (0, 1):
            # if leaving the grid, break
            if col + direction[1] >= len(lines[row]):
                break
            if lines[row + direction[0]][col + direction[1]] != '#':
                if lines[row + direction[0]][col + direction[1]] != 'X':
                    count += 1
                lines[row] = lines[row][:col] + 'X' + lines[row][col + 1:]
                col += direction[1]
            elif lines[row + direction[0]][col + direction[1]] == '#':
                direction = (1, 0)
                # print(f"changing direction, count is {count}")
        elif direction == (1, 0):
            # if leaving the grid, break
            if row + direction[0] >= len(lines):
                break
            if lines[row + direction[0]][col + direction[1]] != '#':
                if lines[row + direction[0]][col + direction[1]] != 'X':
                    count += 1
                lines[row] = lines[row][:col] + 'X' + lines[row][col + 1:]
                row += direction[0]
            elif lines[row + direction[0]][col + direction[1]] == '#':
                direction = (0, -1)
                # print(f"changing direction, count is {count}")
        elif direction == (0, -1):
            # if leaving the grid, break
            if col + direction[1] < 0:
                break
            if lines[row + direction[0]][col + direction[1]] != '#':
                if lines[row + direction[0]][col + direction[1]] != 'X':
                    count += 1
                lines[row] = lines[row][:col] + 'X' + lines[row][col + 1:]
                col += direction[1]
            elif lines[row + direction[0]][col + direction[1]] == '#':
                direction = (-1, 0)
                # print(f"changing direction, count is {count}")
        

    print(count)
    print()
    print()


    lines = [line.strip() for line in open("input.txt")]
    row = starting_row
    col = starting_col

    # up = defaultdict(int)
    # down = defaultdict(lambda: float('inf'))
    # left = defaultdict(int)
    # right = defaultdict(lambda: float('inf'))
    up = {}
    down = {}
    left = {}
    right = {}

    up[starting_col] = starting_row


    direction = (-1, 0)

    num_obstacles = 0
    lines[starting_row] = lines[starting_row][:starting_col] + 'X' + lines[starting_row][starting_col + 1:]
    
    while 0 <= row < len(lines) and 0 <= col < len(lines[row]):
        # print(f"guard at {row}, {col}, pointing {direction}, num_obstacles {num_obstacles}")
        if direction == (-1, 0):
            if row + direction[0] < 0:
                break
            if lines[row + direction[0]][col + direction[1]] != '#':
                if row in right:# and right[row] >= col:
                    # print(f'potential loop')
                    if check_can_reach(row, col, row, right[row], lines):
                        num_obstacles += 1

                lines[row] = lines[row][:col] + 'X' + lines[row][col + 1:]
                row += direction[0]
            elif lines[row + direction[0]][col + direction[1]] == '#':
                direction = (0, 1)
                if row not in right:
                    right[row] = col
                right[row] = min(right[row], col)


        elif direction == (0, 1):
            if col + direction[1] >= len(lines[row]):
                break
            if lines[row + direction[0]][col + direction[1]] != '#':
                if col in down:# and down[col] >= row:
                    # print(f'potential loop')
                    if check_can_reach(row, col, down[col], col, lines):
                        num_obstacles += 1

                lines[row] = lines[row][:col] + 'X' + lines[row][col + 1:]
                col += direction[1]
            elif lines[row + direction[0]][col + direction[1]] == '#':
                direction = (1, 0)
                if col not in down:
                    down[col] = row
                down[col] = min(down[col], row)


        elif direction == (1, 0):
            if row + direction[0] >= len(lines):
                break
            if lines[row + direction[0]][col + direction[1]] != '#':
                if row in left:# and left[row] <= col:
                    # print(f'potential loop')
                    if check_can_reach(row, col, row, left[row], lines):
                        num_obstacles += 1

                lines[row] = lines[row][:col] + 'X' + lines[row][col + 1:]
                row += direction[0]
            elif lines[row + direction[0]][col + direction[1]] == '#':
                direction = (0, -1)
                if row not in left:
                    left[row] = col
                left[row] = max(left[row], col)


        elif direction == (0, -1):
            if col + direction[1] < 0:
                break
            if lines[row + direction[0]][col + direction[1]] != '#':
                if col in up:# and up[col] <= row:
                    # print(f'potential loop')
                    if check_can_reach(row, col, up[col], col, lines):
                        num_obstacles += 1

                lines[row] = lines[row][:col] + 'X' + lines[row][col + 1:]
                col += direction[1]
            elif lines[row + direction[0]][col + direction[1]] == '#':
                direction = (-1, 0)
                if col not in up:
                    up[col] = row
                up[col] = max(up[col], row)

    print(up)
    print(down)
    print(left)
    print(right)
    print(num_obstacles)


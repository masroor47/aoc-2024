


if __name__ == '__main__':
    lines = [line.strip() for line in open("test.txt")]

    key = "XMAS"
    key_backward = key[::-1]
    total = 0
    # horizontal count
    for line in lines:
        # how many times key appears in line
        total += line.count(key)
        total += line.count(key_backward)
        
    print('after horizontal search', total)
    # vertical search
    # stitch strings vertically
    chars = [list(line) for line in lines]
    vertical = list(zip(*chars))
    vertical = ["".join(line) for line in vertical]

    for line in vertical:
        total += line.count(key)
        total += line.count(key_backward)

    print("after vertical search", total)

    for r in range(len(lines[:-3])):
        for c in range(len(lines[0])-3):
            # right down
            if lines[r][c] + lines[r+1][c+1] + lines[r+2][c+2] + lines[r+3][c+3] == key:
                total += 1
            if lines[r][c] + lines[r+1][c+1] + lines[r+2][c+2] + lines[r+3][c+3] == key_backward:
                total += 1
            # left down
            if lines[r][c+3] + lines[r+1][c+2] + lines[r+2][c+1] + lines[r+3][c] == key:
                total += 1
            if lines[r][c+3] + lines[r+1][c+2] + lines[r+2][c+1] + lines[r+3][c] == key_backward:
                total += 1

    print("final", total)
    print()

    # part 2

    key = "MAS"
    key_backward = key[::-1]
    total = 0
    for r in range(len(lines[:-2])):
        for c in range(len(lines[0]) - 2):
            right_down = lines[r][c] + lines[r+1][c+1] + lines[r+2][c+2]
            if right_down == key or right_down == key_backward:
                left_down = lines[r+2][c] + lines[r+1][c+1] + lines[r][c+2]
                if left_down == key or left_down == key_backward:
                    total += 1


    print('part 2', total)
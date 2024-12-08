
def get_starting_position(lines):
    for row, line in enumerate(lines):
        if (col := line.find('^')) != -1:
            return row, col
        
def part1(fn: str):
    # time part 1
    import time
    start_time = time.time()

    lines = [line.strip() for line in open(fn)]
    row, col = get_starting_position(lines)
    lines = [list(line) for line in lines]
    
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0
    good_spots = {(row, col)}
    
    while True:
        next_row = row + moves[dir][0]
        next_col = col + moves[dir][1]
        
        if not (0 <= next_row < len(lines) and 0 <= next_col < len(lines[0])):
            break
            
        if lines[next_row][next_col] != '#':
            row, col = next_row, next_col
            good_spots.add((row, col))
            lines[row][col] = 'X'
        else:
            dir = (dir + 1) % 4
    print(f"Time taken: {time.time() - start_time}")
    return len(good_spots)

def part2(fn: str):
    lines = [line.strip() for line in open(fn)]
    start_row, start_col = get_starting_position(lines)
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # Brute goddamn force you son of a bitch
    total = 0
    total_iterations = len(lines) * len(lines[0])
    from tqdm import tqdm
    with tqdm(total=total_iterations, desc="Processing positions") as pbar:
        for r in range(len(lines)):
            for c in range(len(lines[0])):
                new_lines = [list(line) for line in lines]
                if new_lines[r][c] == '#': continue # already blocked, no need bro
                new_lines[r][c] = '#'

                dir = 0
                orientations = [[-1] * len(lines[0]) for _ in range(len(lines))]
                orientations[start_row][start_col] = 0
                row, col = start_row, start_col

                while True:
                    next_row = row + moves[dir][0]
                    next_col = col + moves[dir][1]

                    if not (0 <= next_row < len(lines) and 0 <= next_col < len(lines[0])):
                        break

                    if orientations[next_row][next_col] == dir: # created a loop
                        total += 1
                        break

                    if new_lines[next_row][next_col] != '#':
                        row, col = next_row, next_col
                        orientations[row][col] = dir
                    else:
                        dir = (dir + 1) % 4
                    # orientations[row][col] = dir

                pbar.update(1)
                
    return total



if __name__ == '__main__':
    
    print(part1("input.txt"))
    print(part2("input.txt"))
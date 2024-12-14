from collections import defaultdict, Counter
import re


def part1(fn):
    lines = [line.strip() for line in open(fn)]

    robots = []
    for line in lines:
        # extract p and v values that are formatted like p=0,4 v=3,-3
        p = list(map(int, re.findall(r'-?\d+', line)))
        curr = [p[:2], p[2:]]
        robots.append(curr)

    width = 101
    height = 103

    '''for test case'''
    # width = 11
    # height = 7
    # robots = [[[2,4], [2, -3]]]
    '''end test case'''

    # numbers are saved as [x, y] and [dx, dy]
    for i in range(100):
        for i in range(len(robots)):
            Pos, Vel = robots[i]
            new_x = (Pos[0] + Vel[0]) % width
            new_y = (Pos[1] + Vel[1]) % height
            robots[i][0][0] = new_x
            robots[i][0][1] = new_y

    quadrants = [0] * 4
    mid_x = width // 2
    mid_y = height // 2

    for Pos, Vel in robots:
        x, y = Pos
        if x in range(0, mid_x):
            if y in range(0, mid_y):
                quadrants[0] += 1
            elif y in range(mid_y+1, height):
                quadrants[1] += 1
        elif x in range(mid_x+1, width):
            if y in range(0, height//2):
                quadrants[2] += 1
            elif y in range(mid_y+1, height):
                quadrants[3] += 1

    print(quadrants)

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]



def part2(fn):
    lines = [line.strip() for line in open(fn)]

    robots = []
    for line in lines:
        p = list(map(int, re.findall(r'-?\d+', line)))
        curr = [p[:2], p[2:]]
        robots.append(curr)

    width = 101
    height = 103

    for t in range(10000):
        for i in range(len(robots)):
            Pos, Vel = robots[i]
            new_x = (Pos[0] + Vel[0]) % width
            new_y = (Pos[1] + Vel[1]) % height
            robots[i][0][0] = new_x
            robots[i][0][1] = new_y
    
        if t < -1000: continue

        grid = [[' '] * width for _ in range(height)]
        for Pos, Vel in robots:
            x, y = Pos
            if grid[y][x] == ' ':
                grid[y][x] = 1
            else:
                grid[y][x] += 1
        print(f"Picture at {t+1} seconds")

        for row in grid:
            print(''.join(map(str, row)))        

        input()


if __name__ == '__main__':
    # print(part1('input.txt'))
    print(part2('input.txt'))
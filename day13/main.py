import re
import numpy as np


def is_whole(x):
    return np.abs(x - np.round(x)) < 1e-10

def part1(fn):
    lines = [line.strip() for line in open(fn)]

    probs = []
    curr_ = []

    for i, line in enumerate(lines):
        if i % 4 == 3:
            probs.append(curr_)
            curr_ = []
        else:
            nums = re.findall(r'\d+', line)
            nums = list(map(int, nums))
            curr_.append(nums)

    probs.append(curr_)

    total = 0
    for A, B, Prize in probs:
        mtx = np.vstack([A, B]).T
        mtx_inv = np.linalg.inv(mtx)
        sln = np.dot(mtx_inv, Prize)
        if is_whole(sln[0]) and is_whole(sln[1]):
            total += round(sln[0]) * 3 + round(sln[1])
    return total


def verify_solution(A, x, b, tolerance=1e-17):
    computed_b = np.dot(A, np.round(x))
    relative_error = np.abs((computed_b - b) / b)
    return np.all(relative_error < tolerance)

def part2(fn):
    lines = [line.strip() for line in open(fn)]

    probs = []
    curr_ = []
    for i, line in enumerate(lines):
        if i % 4 == 3:
            probs.append(curr_)
            curr_ = []
        else:
            nums = re.findall(r'\d+', line)
            nums = list(map(int, nums))
            curr_.append(nums)
    probs.append(curr_)

    total = 0
    for A, B, Prize in probs:
        Prize = [i + 10000000000000 for i in Prize]
        mtx = np.vstack([A, B]).T
        mtx_inv = np.linalg.inv(mtx)
        sln = np.dot(mtx_inv, Prize)
        if verify_solution(mtx, sln, Prize):
            total += round(sln[0]*3 + sln[1])
    return total



if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))
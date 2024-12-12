from collections import defaultdict, Counter

from tqdm import tqdm

def part1(file):
    lines = [list(map(int, line.split())) for line in open(file)]
    line = lines[0]

    print(line)

    for _ in tqdm(range(25), desc="Processing"):
        new_line = []
        for i, n in enumerate(line):
            if n == 0:
                new_line.append(1)
            elif (str_len := len(str(n))) % 2 == 0:
                new_l = int(str(n)[:str_len//2])
                new_r = int(str(n)[str_len//2:])
                new_line.append(new_l)
                new_line.append(new_r)
            else:
                new_line.append(n * 2024)
        line = new_line[:]
        # print(line)

    return len(line)

from functools import lru_cache


def part2(file):
    lines = [list(map(int, line.split())) for line in open(file)]
    line = lines[0]

    memo = defaultdict(defaultdict)

    def construct_nth_version(num, n):
        # print(f"constructing {num} for {n}")

        if num in memo[0]:
            return memo[0][num]
        
        if n == 0:
            # print(f"returning {[num]}")
            return [num]
        if num in memo[n]:
            # print(f"returning memoized {memo[n][num]}")
            return memo[n][num]

        if num == 0:
            memo[n][num] = construct_nth_version(1, n-1)
        elif (str_len := len(str(num))) % 2 == 0:
            new_l = int(str(num)[:str_len//2])
            new_r = int(str(num)[str_len//2:])
            l_res = construct_nth_version(new_l, n-1)
            r_res = construct_nth_version(new_r, n-1)
            # print(f"l_res + r_res: {l_res + r_res}")
            memo[n][num] = l_res + r_res
        else:
            memo[n][num] = construct_nth_version(num * 2024, n-1)
        # print(f"Returning {memo[n][num]}, level {n}")
        return memo[n][num]
    
    new_line = []
    # for i in tqdm(range(len(line)), desc="Processing"):
    for i in range(len(line)):
        n = line[i]
        new_line += construct_nth_version(n, 75)
        # break

    # print(new_line)
    return len(new_line)

# def construct_nth_version(num, n, memo=None):
#     if n == 0:
#         print('reached 0')
#     if memo is None:
#         memo = {}
    
#     # Create a unique key for the (number, iterations) pair
#     key = (num, n)
    
#     # Base case: no more iterations needed
#     if n == 0:
#         return [num]
        
#     # Check if we've already computed this result
#     if key in memo:
#         return memo[key]
        
#     # Apply the transformation rules
#     if num == 0:
#         result = construct_nth_version(1, n-1, memo)
#     elif len(str(num)) % 2 == 0:  # Even number of digits
#         str_num = str(num)
#         mid = len(str_num) // 2
#         left_num = int(str_num[:mid])
#         right_num = int(str_num[mid:])
        
#         # Get transformations for both halves
#         left_result = construct_nth_version(left_num, n-1, memo)
#         right_result = construct_nth_version(right_num, n-1, memo)
        
#         result = left_result + right_result
#     else:  # Odd number of digits
#         result = construct_nth_version(num * 2024, n-1, memo)
    
#     # Store the result in memo before returning
#     memo[key] = result
#     return result


# def part2(file):
#     line = [int(n) for n in open(file).read().split()[0]]
#     result = []
#     iterations = 75
#     for num in tqdm(line, desc="Processing numbers"):
#         result.extend(construct_nth_version(num, iterations))
#     return len(result)
    



if __name__ == '__main__':
    # print(part1('input.txt'))
    print(part2('input.txt'))
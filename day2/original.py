# original file, didn't change after submission

def check_row(line):
    monotonic = True
    diff_check = True
    num_issues = 0
    diffs = [n - line[i+1] for i, n in enumerate(line[:-1])]

    # ensure all nums are all positive or all negative
    if not all(d > 0 for d in diffs) and not all (d < 0 for d in diffs):
        monotonic = False
        num_issues += 1
        # print('didn\'t pass monotonic check')
    if not all(1 <= abs(d) <= 3 for d in diffs):
        diff_check = False
        num_issues += 1
        # print('didn\'t pass diff check')


    return monotonic and diff_check, num_issues

if __name__ == "__main__":

    print(check_row([8, 6, 4, 4, 1]))

    print('-------------------')
    lines = [list(map(int, line.split())) for line in open("input.txt")]
    # print(lines)

    num_safe = 0
    for r, line in enumerate(lines):
        direction = 1 if line[0] < line[1] else -1
        switched = False
        diff_check = True
        num_issues = 0



        res, num_issues = check_row(line)

        if res:
            num_safe += 1
        elif num_issues in [1, 2]:
            # print(f"row {r} has 1 issue")
            # try removing one element for each element
            for i, n in enumerate(line):
                new_line = line[:i] + line[i+1:]
                res, num_issues = check_row(new_line)
                if res:
                    # print(f'row {r} can is fixed by removing element {i}')
                    num_safe += 1
                    break
        # else:
            # print(f"row {r} has {num_issues} issues")




        # for i, n in enumerate(line[:-1]):
        #     if direction == 1 and n > line[i + 1]:
        #         direction = -1
        #         switched = True
        #     elif direction == -1 and n < line[i + 1]:
        #         direction = 1
        #         switched = True

        #     if not (1 <= abs(n - line[i+1]) <= 3):
        #         diff_check = False
        #         num_issues += 1

        # if not switched and diff_check:
        #     num_safe += 1

    print(num_safe)

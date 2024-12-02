# clean, pythonic solution

def check_row(line):
    diffs = [n - line[i+1] for i, n in enumerate(line[:-1])]

    monotonic_issue = not all(d > 0 for d in diffs) and not all (d < 0 for d in diffs)
    diff_issue = not all(1 <= abs(d) <= 3 for d in diffs)

    return not monotonic_issue and not diff_issue, monotonic_issue + diff_issue

def fixample_by_removal(line) -> bool:
    is_valid, num_issues = check_row(line)
    if is_valid:
        return True
    if num_issues > 2:
        return False
    return any(check_row(line[:i] + line[i+1:])[0] for i in range(len(line)))

if __name__ == "__main__":
    lines = [list(map(int, line.split())) for line in open("input.txt")]

    # part 1
    print(sum(check_row(line)[0] for line in lines))

    # part 2
    print(sum(fixample_by_removal(line) for line in lines))

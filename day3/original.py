from collections import defaultdict, Counter
import re

if __name__ == "__main__":
    lines = [line.strip() for line in open("input.txt")]

    # match strings that look like mul(x,y)
    mul = re.compile(r"mul\((\d+),(\d+)\)")
    result = 0
    for line in lines:
        result += sum(int(x) * int(y) for x, y in re.findall(mul, line))
    print(f"part 1: {result}\n")

    # part 2

    in_str = "".join(lines)

    # enabled by default until the first don't() 
    before = in_str.split("don't()")[0]
    total = sum(int(x) * int(y) for x, y in re.findall(mul, before))

    after = "don't()".join(in_str.split("don't()")[1:])

    do_chunks = after.split("do()")[1:] # skip the first chunk because it follows a don't()
    for chunk in do_chunks:
        # initial chunk which is right after a do() but before a don't()
        valid = chunk.split("don't()")[0]
        total += sum(int(x) * int(y) for x, y in re.findall(mul, valid))

    print("original solution", total)


    # position based
    pos = 0
    enabled = True
    total = 0
    
    while pos < len(in_str):
        mul_match = re.search(r'mul\((\d+),(\d+)\)', in_str[pos:])
        dont_match = in_str[pos:].find("don't()")
        do_match = in_str[pos:].find("do()")
        
        next_pos = float('inf')
        if mul_match:
            next_pos = min(next_pos, pos + mul_match.start())
        if dont_match != -1:
            next_pos = min(next_pos, pos + dont_match)
        if do_match != -1:
            next_pos = min(next_pos, pos + do_match)
            
        if next_pos == float('inf'):
            break
            
        if in_str[next_pos:].startswith("don't()"):
            enabled = False
            pos = next_pos + 6
        elif in_str[next_pos:].startswith("do()"):
            enabled = True
            pos = next_pos + 4
        else:
            if enabled:
                x, y = mul_match.groups()
                total += int(x) * int(y)
            pos = next_pos + mul_match.end() - mul_match.start()
            
    print("position based", total)

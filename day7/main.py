from collections import defaultdict, Counter
from tqdm import tqdm


def part_one(eqns):
    ops = {
        0: lambda x, y: x + y,
        1: lambda x, y: x * y,
    }

    total = 0
    for eqn in tqdm(eqns, desc="Processing equations"):
        # try every combination of ops between the args
        result = eqn[0]
        args = eqn[1]
        len(args)
        operations = [0] * (len(args) - 1)
        curr_operator_idx = len(args) - 2  # Start with rightmost operator
    
        # iterate through all possible combinations of operations
        while True:
            # calculate the result of the equation
            curr = args[0]
            for i in range(1, len(args)):
                curr = ops[operations[i-1]](curr, args[i])
                
            if curr == result:
                # print
                total += result
                break
                
            # increment one operation at current index
            operations[curr_operator_idx] += 1
            
            # if current position exceeds max value (1)
            if operations[curr_operator_idx] > 1:
                operations[curr_operator_idx] = 0  # reset current position
                curr_operator_idx -= 1  # move left
                
                # if we've gone through all positions, we're done
                if curr_operator_idx < 0:
                    break
            else:
                # reset to rightmost position for next iteration
                curr_operator_idx = len(args) - 2


    return total

def part_two(eqns):
    ops = {
        0: lambda x, y: x + y,
        1: lambda x, y: x * y,
        2: lambda x, y: int(str(x) + str(y)),
    }

    total = 0

    for eqn in tqdm(eqns, desc="Processing equations"):
        # try every combination of ops between the args
        result = eqn[0]
        args = eqn[1]
        len(args)
        operations = [0] * (len(args) - 1)
        curr_operator_idx = len(args) - 2  # Start with rightmost operator
    
        # iterate through all possible combinations of operations
        while True:
            # calculate the result of the equation
            curr = args[0]
            for i in range(1, len(args)):
                curr = ops[operations[i-1]](curr, args[i])
                
            if curr == result:
                # print
                total += result
                break
                
            # increment one operation at current index
            operations[curr_operator_idx] += 1
            
            # if current position exceeds max value (1)
            if operations[curr_operator_idx] > 2:
                operations[curr_operator_idx] = 0  # reset current position
                curr_operator_idx -= 1  # move left
            
                # if we've gone through all positions, we're done
                if curr_operator_idx < 0:
                    break
            else:
                # reset to rightmost position for next iteration
                curr_operator_idx = len(args) - 2


    return total


if __name__ == '__main__':
    lines = [line.strip() for line in open("input.txt")]

    eqns = []
    for line in lines:
        res, args = line.split(': ')
        res = int(res)
        args = tuple(map(int, args.split(" ")))
        eqns.append((res, args))

    print(f"part 1: {part_one(eqns)}")
    print(f"part 2: {part_two(eqns)}")
    
from collections import defaultdict, Counter
from multiprocessing import Pool
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

def process_equation(eqn):
    ops = {
        0: lambda x, y: x + y,
        1: lambda x, y: x * y,
        2: lambda x, y: int(str(x) + str(y)),
    }
    
    result = eqn[0]
    args = eqn[1]
    operations = [0] * (len(args) - 1)
    curr_operator_idx = len(args) - 2

    while True:
        # calculate the result of the equation
        curr = args[0]
        for i in range(1, len(args)):
            curr = ops[operations[i-1]](curr, args[i])
            
        if curr == result:
            return result
            
        # increment one operation at current index
        operations[curr_operator_idx] += 1
        
        if operations[curr_operator_idx] > 2:
            operations[curr_operator_idx] = 0
            curr_operator_idx -= 1
        
            if curr_operator_idx < 0:
                return 0  # No solution found
        else:
            curr_operator_idx = len(args) - 2

def part_two_multiprocess(eqns):
    # Create process pool using all available cores
    with Pool() as pool:
        # Process equations in parallel with progress bar
        results = list(tqdm(
            pool.imap(process_equation, eqns),
            total=len(eqns),
            desc="Processing equations"
        ))
    
    return sum(results)


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
    print(f"part 2 (multiprocess): {part_two_multiprocess(eqns)}")
    
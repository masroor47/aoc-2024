from collections import defaultdict, Counter


def check_if_good(day, before, after):
    for i, curr_page in enumerate(day):
        
        for j, before_page in enumerate(day[:i]):
            if before_page in before[curr_page]:
                return False

        for j, after_page in enumerate(day[i+1:]):
            if after_page in after[curr_page]:
                return False

    return True

if __name__ == '__main__':
    lines = [line.strip() for line in open("input.txt")]


    for i in range(len(lines)):
        if lines[i] == '':
            rules, rest = lines[:i], lines[i+1:]

    rules = [rule.split('|') for rule in rules]
    # print(rules)
    rest = [line.split(',') for line in rest]
    # print(rest)

    before = defaultdict(set)
    after = defaultdict(set)

    for rule in rules:
        prior, post = rule
        # print(prior, post)
        before[prior].add(post)
        after[post].add(prior)


    total = 0
    for day in rest:
        # print(f"current set of pages: {day}")
        good = True
        for i, curr_page in enumerate(day):
            
            for j, before_page in enumerate(day[:i]):
                if before_page in before[curr_page]:
                    good = False
                    break

            for j, after_page in enumerate(day[i+1:]):
                if after_page in after[curr_page]:
                    good = False
                    break

        if good:
            # print(f"good page order: {day}")
            total += int(day[len(day)//2])

        # break

    print(total)

    # part 2


    # --------------------

    total = 0
    for day in rest:
        # print(f"current set of pages: {day}")
        good = True
        for i, curr_page in enumerate(day):
            
            before_break_idx = None
            after_break_idx = None

            for j, before_page in enumerate(day[:i]):
                if before_page in before[curr_page]:
                    good = False
                    before_break_idx = j
                    break

            for j, after_page in enumerate(day[i+1:]):
                if after_page in after[curr_page]:
                    good = False
                    after_break_idx = j
                    break

        if not good:
            new_day = day[:]

            # # update order of the page
            # while not good:
            #     pass

            while True:
                swaps_made = 0
                
                # Check each rule
                for i, j in rules:
                    # Only process if both elements are in our list
                    if i in new_day and j in new_day:
                        before_idx = new_day.index(i)
                        after_idx = new_day.index(j)
                        
                        # If the rule is violated (before comes after), swap them
                        if before_idx > after_idx:
                            # Swap the elements
                            new_day[before_idx], new_day[after_idx] = new_day[after_idx], new_day[before_idx]
                            swaps_made += 1
                
                # If no swaps were needed, we're done
                if swaps_made == 0:
                    break
            


            total += int(new_day[len(new_day)//2])


    print(total)

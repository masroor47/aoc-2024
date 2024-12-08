from collections import defaultdict, Counter


if __name__ == '__main__':
    lines = [line.strip() for line in open("input.txt")]

    letter_location = defaultdict(list)

    for r, line in enumerate(lines):
        for i, c in enumerate(line):
            if c.isalnum():
                letter_location[c].append((r, i))

    print(letter_location.keys())
    print(letter_location)

    total = 0
    unique_locations = set()
    for letter, locations in letter_location.items():
        # iterate over every pair combination of locations
        for i, loc1 in enumerate(locations):
            for loc2 in locations[i+1:]:
                print()
                print(loc1, loc2)
                # top point
                dr = loc2[0] - loc1[0]
                dc = loc2[1] - loc1[1]
                # print(f"dr: {dr}, dc: {dc}")
                r = min(loc1[0], loc2[0]) - abs(dr)
                c = None
                if r >= 0:
                    slope = dr*dc
                    if slope > 0:
                        c = min(loc1[1], loc2[1]) - abs(dc)
                        if c >= 0:
                            total += 1
                            unique_locations.add((r, c))
                    else:
                        c = max(loc1[1], loc2[1]) + abs(dc)
                        if c < len(lines[0]):
                            total += 1
                            unique_locations.add((r, c))

                # bottom point
                r = max(loc1[0], loc2[0]) + abs(dr)
                if r < len(lines):
                    slope = dr*dc
                    if slope > 0:
                        c = max(loc1[1], loc2[1]) + abs(dc)
                        if c < len(lines[0]):
                            total += 1
                            unique_locations.add((r, c))
                    else:
                        c = min(loc1[1], loc2[1]) - abs(dc)
                        if c >= 0:
                            total += 1
                            unique_locations.add((r, c))

    # lines = [list(line) for line in lines]
    # for r, c in unique_locations:
    #     r = int(r)
    #     c = int(c)
    #     lines[r][c] = "#"
    
    # for line in lines:
    #     print("".join(line))

    print(f"Total: {len(unique_locations)}")



    total = 0
    unique_locations = set()
    for letter, locations in letter_location.items():
        # iterate over every pair combination of locations
        for i, loc1 in enumerate(locations):
            for loc2 in locations[i+1:]:
                print(loc1, loc2)
                unique_locations.add(loc1)
                unique_locations.add(loc2)

                # top point
                dr = loc2[0] - loc1[0]
                dc = loc2[1] - loc1[1]
                slope = dr*dc
                # top point
                if slope >= 0:
                    r = min(loc1[0], loc2[0]) - abs(dr)
                    c = min(loc1[1], loc2[1]) - abs(dc)
                    while True:
                        print(f"check r: {r}, c: {c}")
                        if r < 0 or c < 0:
                            break
                        unique_locations.add((r, c))
                        r -= abs(dr)
                        c -= abs(dc)
                else:
                    r = min(loc1[0], loc2[0]) - abs(dr)
                    c = max(loc1[1], loc2[1]) + abs(dc)
                    while True:
                        if r < 0 or c >= len(lines[0]):
                            break
                        unique_locations.add((r, c))
                        r -= abs(dr)
                        c += abs(dc)

                # bottom point
                if slope >= 0:
                    r = max(loc1[0], loc2[0]) + abs(dr)
                    c = max(loc1[1], loc2[1]) + abs(dc)
                    while True:
                        
                        if r >= len(lines) or c >= len(lines[0]):
                            break
                        unique_locations.add((r, c))
                        # print(f'adding ({r},{c})')
                        r += abs(dr)
                        c += abs(dc)
                else:
                    r = max(loc1[0], loc2[0]) + abs(dr)
                    c = min(loc1[1], loc2[1]) - abs(dc)
                    while True:
                        if r >= len(lines) or c < 0:
                            break
                        unique_locations.add((r, c))
                        r += abs(dr)
                        c -= abs(dc)

    lines = [list(line) for line in lines]
    for r, c in unique_locations:
        r = int(r)
        c = int(c)
        lines[r][c] = "#"
    
    for line in lines:
        print("".join(line))

    print(f"Total: {len(unique_locations)}")



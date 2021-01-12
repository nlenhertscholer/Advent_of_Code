with open("route.txt") as f:
    route = f.readlines()
    tree_count = 0
    
    # remove new line chars
    for i, row in enumerate(route):
        route[i] = row[:-1]

    x, y = 0, 0
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    x3, y3 = 0, 0
    x4, y4 = 0, 0
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0

    for row in route:
        # Part 1
        x = (x + 3) % len(row)
        y += 1
        if y < len(route):
            if route[y][:x+1][-1] == '#':
                n1 += 1
        
        # Part two
        x1 = (x1 + 1) % len(row)
        y1 += 1
        if y1 < len(route):
            if route[y1][:x1+1][-1] == '#':
                n2 += 1

        x2 = (x2 + 5) % len(row)
        y2 += 1
        if y2 < len(route):
            if route[y2][:x2+1][-1] == '#':
                n3 += 1

        x3 = (x3 + 7) % len(row)
        y3 += 1
        if y3 < len(route):
            if route[y3][:x3+1][-1] == '#':
                n4 += 1

        x4 = (x4 + 1) % len(row)
        y4 += 2
        if y4 < len(route):
            if route[y4][:x4+1][-1] == '#':
                n5 += 1

print("Part 1:", n1)
print("Part 2:", n1 * n2 * n3 * n4 * n5)




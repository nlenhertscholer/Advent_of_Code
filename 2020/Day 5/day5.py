def decode(bpass):
    rowLower = 0
    rowUpper = 127
    for char in bpass[0:7]:
        if char == 'F':
            rowUpper = (rowLower + rowUpper) // 2 
        else:
            rowLower = (rowLower + rowUpper) // 2 + 1

    colLower = 0
    colHigher = 7
    for char in bpass[7:]:
        if char == 'L':
            colHigher = (colLower + colHigher) // 2
        else:
            colLower = (colLower + colHigher) // 2 + 1
    
    return rowUpper, colHigher

with open("Day 5/passes.txt") as f:
    passes = f.readlines()

# maxID = 0
ids = []
for bpass in passes:
    row, col = decode(bpass)
    tmp = row * 8 + col
    # if tmp > maxID:
    #     maxID = 
    ids.append(tmp)
# print(maxID)
# ids.sort()
for i in range(36, 945):
    if i not in ids:
        print(i)
        exit(1)
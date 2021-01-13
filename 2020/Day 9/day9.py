with open("Day 9/numbers.txt") as f:
    # Read in numbers from the file and convert to int data type
    numbers = []
    while True:
        num = f.readline()
        if not num:
            break
        numbers.append(int(num))

preamble = numbers[:25]
goal = 0
# Part 1
for target_num in numbers[25:]:
    has_sum = False

    for x in preamble:
        for y in preamble:
            if x != y and x + y == target_num:
                has_sum = True
                break

        if has_sum:
            break
    
    preamble.pop(0)
    preamble.append(target_num)
    if not has_sum:
        print("First number not matching pattern:", target_num)
        goal = target_num
        break

# Part 2
idx = numbers.index(goal)
for num_elements in range(2, idx):
    for shift in range(idx-num_elements+1):
        candidates = numbers[shift:shift+num_elements]
        
        if sum(candidates) == goal:
            print("Weakness is:", min(candidates) + max(candidates))
            exit(0)
with open("Day 6/answers.txt") as file:
    total = 0
    yes_answers = set()
    group = []
    while True:
        line = file.readline()

        if line == '\n' or not line:
            intersect = set.intersection(*group)        # Unpack the list into separate arguments
            total += len(intersect)
            group = []
            if not line:
                break
            else:
                continue
        
        yes_answers = set()
        for answer in line:
            if answer != "\n":
                yes_answers.add(answer)
        group.append(yes_answers)
print(total)
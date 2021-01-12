with open("passwords.txt") as f:
    correct = 0
    while True:
        line = f.readline()
        if not line:
            print(correct)
            exit(0)
        
        data = line.split(" ")

        min = int(data[0].split('-')[0])
        max = int(data[0].split('-')[1])

        target_char = data[1][0]
        
        password = data[2]
        
        # Part 1, occurances within a range
        # occurances = password.count(target_char)
        # if occurances >= min and occurances <= max:
        #     correct += 1

        # Part 2, exact positions
        if password[min-1] == target_char and password[max-1] != target_char:
            correct += 1
        elif password[min-1] != target_char and password[max-1] == target_char:
            correct += 1
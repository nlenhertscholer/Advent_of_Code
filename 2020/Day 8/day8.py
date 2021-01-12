with open("Day 8/bootcode.txt") as f:
    code = f.readlines()


j = 0
ended = False
operation = ""
argument = ""
# This outer while loop is part 2 and it brute forces this solution
while not ended:

    if j != 0 and j < len(code):
        if operation == "jmp":
            operation = "nop"
        else:
            operation = "jmp"
        code[j] = operation + " " + argument
        j += 1

    while True:
        if j < len(code):
            operation, argument = code[j].split(" ")[0], code[j].split(" ")[1]
            if operation == "jmp" or operation == "nop":
                if operation == "jmp":
                    operation = "nop"
                else:
                    operation = "jmp"
                code[j] = operation + " " + argument
                break
            
            j += 1
        else:
            break

    # This while loop is part 1
    i = 0
    acc = 0
    seen_lines = {}
    while True:
        if i >= len(code):
            ended = True
            break
        op, arg = code[i].split(" ")[0], code[i].split(" ")[1]

        if i in seen_lines:
            ended = False
            break  
        else:
            seen_lines[i] = 0

        if op == "acc":
            acc += int(arg)
        elif op == "jmp":
            i += int(arg)   
            continue  
        elif op == "nop":
            pass

        i += 1

print(acc)
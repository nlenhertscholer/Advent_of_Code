# Given a list of integers, multiply together the two numbers that add up to 2020
with open("expense_report.txt") as f:
    report = f.readlines()

for i, line in enumerate(report):
    report[i] = int(line)

for i, num1 in enumerate(report):
    for j, num2 in enumerate(report):
        if i != j:
            if num1 + num2 == 2020:
                print(f"Two Numbers: {num1 * num2}")

            # Extension for part 2
            for k, num3 in enumerate(report):
                if i != k and j != k:
                    if num1 + num2 + num3 == 2020:
                        print(f"Three Numbers: {num1 * num2 * num3}")    
                        exit(0)        
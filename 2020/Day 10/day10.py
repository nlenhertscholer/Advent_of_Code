with open("Day 10/joltages.txt") as f:
    joltages = []
    while True:
        next_joltage = f.readline()

        if not next_joltage:
            break

        joltages.append(int(next_joltage))

joltages = sorted(joltages)
joltages.append(joltages[-1] + 3)

one_jolt_diff = 0
three_jolt_diff = 0
joltage = 0

for jolt in joltages:
    diff = jolt - joltage
    if diff == 1:
        one_jolt_diff += 1
    elif diff == 3:
        three_jolt_diff += 1
    elif diff > 3:
        continue

    joltage = jolt

print("Part 1:", one_jolt_diff * three_jolt_diff)


# Part 2
sol = {0:1}
for jolt in joltages:
    sol[jolt] = 0

    if jolt - 1 in sol:
        sol[jolt] += sol[jolt - 1]

    if jolt - 2 in sol:
        sol[jolt] += sol[jolt - 2]

    if jolt - 3 in sol:
        sol[jolt] += sol[jolt - 3]

print("Part 2:", sol[joltages[-1]])



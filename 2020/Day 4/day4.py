tags = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

with open("Day 4/passports.txt") as f:
    lines = f.readlines()

passports = []
i = 0
for line in lines:
    if line == '\n':
        i += 1
        continue
    if len(passports) == i:
        passports.append(line.replace('\n', ' '))
    else:
        passports[i] = passports[i] + line.replace('\n', ' ')

num_correct = 0
for passport in passports:
    passport.replace("\n", "")
    is_correct = True
    for tag in tags:
        if tag not in passport and tag != "cid":
            is_correct = False
            break
    if is_correct:
        # Part 2
        fields = passport.split(" ")
        for field in fields:
            if field[:3] == "byr":
                if int(field[4:]) < 1920 or int(field[4:]) > 2002:
                    is_correct = False
            elif field[:3] == "iyr":
                if int(field[4:]) < 2010 or int(field[4:]) > 2020:
                    is_correct = False
            elif field[:3] == "eyr":
                if int(field[4:]) < 2020 or int(field[4:]) > 2030:
                    is_correct = False
            elif field[:3] == "hgt":
                if field[-2:] == "cm":
                    if int(field[4:-2]) < 150 or int(field[4:-2]) > 193:
                        is_correct = False
                elif field[-2:] == "in":
                    if int(field[4:-2]) < 59 or int(field[4:-2]) > 76:
                        is_correct = False
                else:
                    is_correct = False
            elif field[:3] == "hcl":
                if field[4] == "#":
                    if len(field[5:]) != 6:
                        is_correct = False
                    else:
                        for c in field[5:]:
                            if not c.isnumeric() and ord(c) > ord('f'):
                                is_correct = False
                else:
                    is_correct = False
            elif field[:3] == "ecl":
                valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if field[4:] not in valid:
                    is_correct = False
            elif field[:3] == "pid":
                if len(field[4:]) != 9 or not field[4:].isnumeric():
                    is_correct = False
        
        if is_correct:
            num_correct += 1

print(num_correct)
    
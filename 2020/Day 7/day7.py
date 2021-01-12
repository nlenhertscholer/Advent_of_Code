with open("Day 7/bag_rules.txt", 'r') as f:
    bag_rules = f.readlines()

# ----- Part 1 -----
allowable_bags = {"shiny gold"}

while True:
    new_bags = set()
    for rule in bag_rules:
        srule = rule.split(" bags contain ")
        outer_bag = srule[0]
        inner_bags = srule[1]

        if "no other bags" in inner_bags:
            continue

        for bag in allowable_bags:
            if bag in inner_bags and outer_bag not in allowable_bags:
                new_bags.add(outer_bag)

    if len(new_bags) == 0:
        break
    else:
        allowable_bags = allowable_bags.union(new_bags)

print("Number of bags that will eventually contain shiny gold bag:", len(allowable_bags))


# ----- Part 2 -----
def search(outer_bag, inner_bags):
    if inner_bags == 0:
        return 0
    
    amount_to_contain = 0
    for bag, count in inner_bags.items():
        contains = search(bag, rules[bag])
        amount_to_contain += count + count*contains
    
    return amount_to_contain
        

def convert(inner_bags):
    if "no other bags" in inner_bags:
        return 0
    converted_data = {}
    sbags = inner_bags.split(", ")
    for bag in sbags:
        split = bag.split(' ')
        converted_data[split[1] + ' ' + split[2]] = int(split[0])
    return converted_data


rules = {}
for rule in bag_rules:
    srule = rule.split(" bags contain ")
    outer_bag = srule[0]
    inner_bags = srule[1]
    rules[outer_bag] = convert(inner_bags)

print("Shiny gold bag can contain:", search("shiny gold", rules["shiny gold"]))

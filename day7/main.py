import re

with open('input.txt', 'r') as f:
    input = f.read().splitlines()

def clean(rule):
    rule_no_numeric = re.sub(r'[1-9]', '', rule)
    return rule_no_numeric.replace('bags', '').replace('bag', '').replace('.', '').replace(' ', '')

def split(rule):
    split_rule = clean(rule).split('contain')
    return (split_rule[0], split_rule[1].split(','))

bag_to_contents = dict(split(rule) for rule in input)

def check(contents):
    return True if 'shinygold' in contents else False

colours = []

def check_contents(contents, original_bag):
    for content in contents:
        contents_contain = bag_to_contents.get(content, [])
        if check(contents_contain):
            colours.append(original_bag)
        elif contents_contain:
            check_contents(contents_contain, original_bag)

for bag, contents in bag_to_contents.items():
    if 'shinygold' in contents:
        colours.append(bag)
    else:
        check_contents(contents, bag)

print(len(set(colours)))


############## PART 2 #################


def clean(rule):
    return rule.replace('bags', '').replace('bag', '').replace('.', '').replace(' ', '')

def extract_num(rule):
    num = re.match(r'[1-9]', rule)
    return (int(num.group(0)) if num else 0, re.sub(r'[1-9]', '', rule))

def split(rule):
    split_rule = clean(rule).split('contain')
    contents = [dict(zip(['num', 'colour'], extract_num(rule))) for rule in split_rule[1].split(',')]
    return (split_rule[0], contents)

bag_to_contents = dict(split(rule) for rule in input)

tot_bags = []

def check_contents(contents, temp_bags=0, multiplier=1):
    for content in contents:
        tot_bags.append(content['num']*multiplier)
        contents_contain = bag_to_contents.get(content['colour'], [])
        if contents_contain:
            check_contents(contents_contain, temp_bags, content['num']*multiplier)

for bag, contents in bag_to_contents.items():
    temp = sum(tot_bags)
    if bag == 'shinygold':
        check_contents(contents, temp)

print('total bags needed', sum(tot_bags))

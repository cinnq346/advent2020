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

def check_contents(contents):
    for content in contents:
        contents_contain = bag_to_contents.get(content, [])
        if check(contents_contain):
            colours.append(content)
        elif contents_contain:
            check_contents(contents_contain)

for bag, contents in bag_to_contents.items():
    if 'shinygold' in contents:
        colours.append(bag)
    else:
        check_contents(contents)

print(len(set(colours)))

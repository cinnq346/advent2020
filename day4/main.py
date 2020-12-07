import re

with open('input.txt', 'r') as f:
    input = f.read().split('\n\n')

def convert(item):
    return list(filter(None, re.split(' ', item.replace('\n', ' '))))

def to_dict(passport):
    return dict(item.split(':') for item in passport)

input_dicts = [
    to_dict(convert(item))
    for item in input]

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_valid(passport):
    keys = passport.keys()
    filtered_keys = list(filter(lambda x: x != 'cid', keys))
    return True if ((len(filtered_keys) == 7) and all(True for key in filtered_keys if key in required)) else False

print(sum(1 for item in input_dicts if is_valid(item)))

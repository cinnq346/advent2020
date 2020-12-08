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


#################### Part 2

def byr(value):
    return True if ((len(value) == 4) and (int(value) >= 1920) and (int(value) <= 2002)) else False

def iyr(value):
    return True if ((len(value) == 4) and (int(value) >= 2010) and (int(value) <= 2020)) else False

def eyr(value):
    return True if ((len(value) == 4) and (int(value) >= 2020) and (int(value) <= 2030)) else False

def hgt(value):
    cm = re.search(r'^\d+cm$', value)
    inches = re.search(r'^\d+in$', value)
    cm_val = int(cm.group(0).split('cm')[0]) if cm else None
    in_val = int(inches.group(0).split('in')[0]) if inches else None
    return True if ((cm and cm_val >= 150 and cm_val <= 193) or (inches and in_val >= 59 and in_val <= 76)) else False

def hcl(value):
    return True if re.search(r'^#[0-9,a-f]{6}$', value) else False

allowed_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def ecl(value):
    return True if value in allowed_ecl else False

def pid(value):
    return True if re.search(r'^[0-9]{9}$', value) else False


checks = {
    'byr': byr, 'iyr': iyr, 'eyr': eyr, 'hgt': hgt, 'hcl': hcl, 'ecl': ecl, 'pid': pid
}

def is_valid_values(passport):
    keys = passport.keys()
    filtered_keys = list(filter(lambda x: x != 'cid', keys))
    return True if (
        (len(filtered_keys) == 7) and
        all(True if ((key in required) and checks[key](passport[key])) else False for key in filtered_keys)
    ) else False

print(sum(1 for item in input_dicts if is_valid_values(item)))

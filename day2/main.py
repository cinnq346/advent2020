import re

def convert(item):
    return list(filter(None, re.split(':|-', item.replace(' ', ':'))))

def test_comparison(letter, test, idx):
    try:
        return True if letter == test[idx-1] else False
    except:
        return False

with open('input.txt', 'r') as f:
    input = f.read().splitlines()

input_zipped = [
    dict(zip(['first', 'second', 'letter', 'test'], convert(item)))
    for item in input]

success = 0
for item in input_zipped:
    first = test_comparison(item['letter'], item['test'], int(item['first']))
    second = test_comparison(item['letter'], item['test'], int(item['second']))
    if ((first and not second) or (not first and second)):
        success = success + 1

print(success)

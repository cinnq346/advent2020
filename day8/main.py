with open('input.txt', 'r') as f:
    input = f.read().splitlines()

def clean( rule):
    action, value = rule.split(' ')
    return (action, value)

input_enum = [{idx: clean(rule)} for idx, rule in enumerate(input)]

rules_already_seen = []

def endless_recursion(rule, acc):
    idx = list(rule.keys())[0]
    idx_int = int(idx)
    action, value = rule[idx]

    rules_already_seen.append(idx)

    if len(rules_already_seen) > len(set(rules_already_seen)):
        print(acc)
        return

    if action == 'acc':
        acc = acc + int(value)
        endless_recursion(input_enum[idx_int + 1], acc)
    elif action == 'jmp':
        endless_recursion(input_enum[idx_int + int(value)], acc)
    else:
        endless_recursion(input_enum[idx_int + 1], acc)

endless_recursion(input_enum[0], 0)

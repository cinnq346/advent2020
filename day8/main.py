with open('input.txt', 'r') as f:
    input = f.read().splitlines()

def clean(rule):
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

############# PART 2 ###################


def clean(rule):
    action, value = rule.split(' ')
    return (action, value)

input_enum = {idx: clean(rule) for idx, rule in enumerate(input)}

def endless_recursion_with_exit(idx, acc, temp_input_enum, rules_already_seen):
    action, value = temp_input_enum[idx]

    rules_already_seen.append(idx)

    if len(rules_already_seen) > len(set(rules_already_seen)):
        return

    if ((action in ['acc', 'nop']) and (idx == len(input_enum))):
        print(acc)
        return

    if action == 'acc':
        acc = acc + int(value)
        endless_recursion_with_exit(idx + 1, acc, temp_input_enum, rules_already_seen)
    elif action == 'jmp':
        endless_recursion_with_exit(idx + int(value), acc, temp_input_enum, rules_already_seen)
    elif action == 'nop':
        endless_recursion_with_exit(idx + 1, acc, temp_input_enum, rules_already_seen)


for idx, rule in input_enum.items():
    temp_input_enum = input_enum
    action, value = rule
    if action == 'jmp':
        temp_input_enum[idx] = ('nop', value)
    elif action == 'nop':
        temp_input_enum[idx] = ('jmp', value)
    endless_recursion_with_exit(0, 0, temp_input_enum, [])

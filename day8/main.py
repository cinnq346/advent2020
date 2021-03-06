with open('input.txt', 'r') as f:
    input = f.read().splitlines()

def clean(rule):
    action, value = rule.split(' ')
    return (action, value)

input_enum = {idx: clean(rule) for idx, rule in enumerate(input)}

rules_already_seen = []

def endless_recursion(idx, acc):
    action, value = input_enum[idx]

    next_idx = idx + int(value) if action == 'jmp' else idx + 1

    rules_already_seen.append(idx)

    if len(rules_already_seen) > len(set(rules_already_seen)):
        print(acc)
        return

    if action == 'acc':
        acc = acc + int(value)
    endless_recursion(next_idx, acc)

endless_recursion(0, 0)

############# PART 2 ###################

def endless_recursion_with_exit(idx, acc, temp_input_enum, rules_already_seen):
    rules_already_seen.append(idx)
    action, value = temp_input_enum[idx]

    next_idx = idx + int(value) if action == 'jmp' else idx + 1

    if next_idx > max(list(temp_input_enum.keys())):
        print(acc)
        return

    if len(rules_already_seen) > len(set(rules_already_seen)):
        return

    if action == 'acc':
        acc = acc + int(value)
    endless_recursion_with_exit(next_idx, acc, temp_input_enum, rules_already_seen)

for idx, rule in input_enum.items():
    temp_input_enum = input_enum.copy()
    action, value = rule
    if action == 'jmp':
        temp_input_enum[idx] = ('nop', value)
    elif action == 'nop':
        temp_input_enum[idx] = ('jmp', value)

    endless_recursion_with_exit(0, 0, temp_input_enum, [])

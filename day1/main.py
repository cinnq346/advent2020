def print_stuff(one, two, three):
    print(one * two * three)

with open('input.txt', 'r') as f:
    input = f.read().split('\n')

input_int = [int(str) for str in input if str]


for idx in range(len(input_int)):
    [print_stuff(item, input_int[idx], item2) for item2 in input_int[:idx] for item in input_int[idx:] if (input_int[idx] + item + item2 == 2020)]

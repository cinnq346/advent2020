with open('input.txt', 'r') as f:
    input = f.read().splitlines()

input_num = sorted([int(num) for num in input])

ones = 0
threes = 1 # because we always have a diff of 3 between built-in joltage adaptor and highest other adaptor

for idx, num in enumerate(input_num):
    if idx < len(input_num) - 1:
        if input_num[idx+1] - num == 1:
            ones = ones + 1
        elif input_num[idx+1] - num == 3:
            threes = threes + 1

print(ones * threes)

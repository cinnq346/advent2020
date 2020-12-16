with open('input.txt', 'r') as f:
    input = f.read().splitlines()

input_num = [int(num) for num in input]

def check(num, past_25_num):
    return any(True if ((num - test) in past_25_num) else False for test in past_25_num)

for idx, num in enumerate(input_num):
    if idx > 24:
        if check(num, input_num[(idx-25):idx]) == False:
            print(num)
            break

with open('input.txt', 'r') as f:
    input = f.read().splitlines()

input_arr = [list(row) for row in input]

def extend_row(row, idx):
    try:
        if row[idx]:
            return row
    except:
        return extend_row(row+row, idx)

increments = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2}
    ]

multiplied_trees = 1
for inc in increments:
    right_inc = inc['right']
    down_inc = inc['down']
    trees = 0
    right = 0
    for row_idx in range(len(input_arr)):
        if row_idx % down_inc == 0:
            row = input_arr[row_idx]
            if extend_row(row, right)[right] == '#':
                trees = trees + 1
            right = right + right_inc
    multiplied_trees = multiplied_trees * trees

    print(right_inc, down_inc, trees)
print(multiplied_trees)

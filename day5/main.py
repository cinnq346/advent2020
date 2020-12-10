with open('input.txt', 'r') as f:
    input = f.read().splitlines()

input_split = [(seat[:7], seat[7:]) for seat in input]

def find_seat(dimension, max, letter):
    dimension_max = max
    dimension_min = 0
    for dimension_letter in dimension:
        half_way = round((dimension_max-dimension_min)/2)
        if dimension_letter == letter:
            dimension_max = dimension_max - half_way
        else:
            dimension_min = dimension_min + half_way
    return dimension_min if dimension[-1] == letter else dimension_max

seats = [(find_seat(i[0], 127, 'F'), find_seat(i[1], 7, 'L')) for i in input_split]

seat_ids = [ int((seat[0] * 8) + seat[1]) for seat in seats]

print(max(seat_ids))

######## PART 2 ############

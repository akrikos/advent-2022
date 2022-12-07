# find any that completely encompass other
total = 0
with open('input.txt', 'r') as file:
    for line in file:
        # remove \n
        line = line[:-1]
        [left, right] = line.split(',')
        [min_l, max_l] = map(int, left.split('-'))
        [min_r, max_r] = map(int, right.split('-'))
        if (min_l <= min_r and max_l >= max_r) or (min_r <= min_l and max_r >= max_l):
            total += 1

print(total)


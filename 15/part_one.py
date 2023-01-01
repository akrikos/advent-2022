import operator
from functools import reduce

from utils.utils import parse_ints

# line_num = 10
line_num = 2000000
no_beacon_locs = set()
known_beacon_locs = set()

# with open('test_input.txt') as file:
with open('test_input.txt') as file:
    for line in file:
        inputs = parse_ints(line)
        sensor_loc = tuple(inputs[:2])
        beacon_loc = tuple(inputs[2:])
        known_beacon_locs.add(beacon_loc)
        distance = reduce(lambda accum, val: abs(val) + accum, map(operator.sub, sensor_loc, beacon_loc), 0)

        for x in range(-distance, distance + 1):
            max_y = abs(distance - abs(x))
            for y in range(-max_y, max_y + 1):
                no_beacon = tuple(map(operator.add, sensor_loc, (x, y)))
                if no_beacon not in known_beacon_locs:
                    no_beacon_locs.add(no_beacon)

num_locs_in_line = 0
for loc in no_beacon_locs:
    if loc[1] == line_num:
        # print(loc)
        num_locs_in_line += 1

print(f'In row {line_num}, there are {num_locs_in_line} positions where a beacon cannot be.')

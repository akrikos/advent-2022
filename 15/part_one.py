import operator
from functools import reduce

from utils.utils import parse_ints

class Ranges:
    def __init__(self):
        self.ranges = []

    def add_range(self, min_x, max_x):
        old_ranges = self.ranges
        self.ranges = [(min_x, max_x)]
        for r in old_ranges:
            self._add(*r)

    def _add(self, min_x, max_x):
        for i, r in enumerate(self.ranges):
            # r = self.ranges[i]
            if min_x < r[0]:
                if max_x < r[0]:
                    # no overlap, add before
                    self.ranges.insert(i, (min_x, max_x))
                    break
                else:
                    if max_x > r[1]:
                        # wholly contained
                        self.ranges[i] = (min_x, max_x)
                        break
                    else:
                        # overlap, lower left side of r to accomodate
                        self.ranges[i] = (min_x, self.ranges[i][1])
                        break
            else:
                if min_x > r[1]:
                    # no overlap, continue to next, may need to append?
                    if i == len(self.ranges) - 1:
                        self.ranges.append((min_x, max_x))
                        break
                elif max_x <= r[1]:
                    # wholly contained
                    break
                else:
                    # overlap, raise right side of r
                    self.ranges[i] = (self.ranges[i][0], max_x)
                    break

# line_num = 10
line_num = 2000000
no_beacon_locs = set()
known_beacon_locs = set()

ranges_in_line = Ranges()

# with open('test_input.txt') as file:
with open('input.txt') as file:
    for line in file:
        inputs = parse_ints(line)
        sensor_loc = tuple(inputs[:2])
        beacon_loc = tuple(inputs[2:])
        known_beacon_locs.add(beacon_loc)
        distance = reduce(lambda accum, val: abs(val) + accum, map(operator.sub, sensor_loc, beacon_loc), 0)

        # does this even matter to the line we care about?
        if line_num >= (sensor_loc[1] - distance) and line_num <= (sensor_loc[1] + distance):
            y_diff = abs(line_num - sensor_loc[1])
            x_diff = distance - y_diff
            min_x = -x_diff + sensor_loc[0]
            max_x = x_diff + sensor_loc[0]
            ranges_in_line.add_range(min_x, max_x)

num_locs_in_line = 0
for r in ranges_in_line.ranges:
    num_locs_in_line = num_locs_in_line + r[1]-r[0] + 1
    for beacon in known_beacon_locs:
        if beacon[1] == line_num and beacon[0] >= r[0] and beacon[0] <= r[1]:
            num_locs_in_line -= 1


print(f'In row {line_num}, there are {num_locs_in_line} positions where a beacon cannot be.')

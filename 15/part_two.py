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

min_search = 0
# max_search = 20
max_search = 4000000
no_beacon_locs = set()
known_beacon_locs = set()

ranges_by_line = [Ranges() for i in range(min_search, max_search + 1)]
# with open('test_input.txt') as file:
with open('input.txt') as file:
    for line in file:
        inputs = parse_ints(line)
        sensor_loc = tuple(inputs[:2])
        beacon_loc = tuple(inputs[2:])
        known_beacon_locs.add(beacon_loc)
        distance = reduce(lambda accum, val: abs(val) + accum, map(operator.sub, sensor_loc, beacon_loc), 0)

        for i in range(min_search, max_search + 1):
            if i >= (sensor_loc[1] - distance) and i <= (sensor_loc[1] + distance):
                y_diff = abs(i - sensor_loc[1])
                x_diff = distance - y_diff
                min_x = -x_diff + sensor_loc[0]
                max_x = x_diff + sensor_loc[0]
                # if i >= len(ranges_by_line) - 1:
                #     ranges_by_line.append(Ranges())
                ranges_by_line[i].add_range(min_x, max_x)

for y, ranges  in enumerate(ranges_by_line):
    if len(ranges.ranges) > 1:
        # this is deeply flawed. could be more than two ranges since doesn't account for ranges abutting one another
        # but it worked, so /shrug
        print(ranges.ranges[0][1]+ 1, y)
        break

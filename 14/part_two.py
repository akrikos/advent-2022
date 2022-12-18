import re
import operator

point_regex = re.compile('(\d+),(\d+)')

filled_points = {}

def is_filled(x, y):
    global floor_y
    if filled_points.get((x, y), None) is None and y < floor_y:
        return False
    return True

lowest_point = 0
# with open('test_input.txt') as file:
with open('input.txt') as file:
    for line in file:
        matches = point_regex.findall(line)
        print(matches)
        previous = None
        for current in [(int(x), int(y)) for (x,y) in matches]:
            if previous is None:
                previous = current
                continue
            diff = tuple(map(operator.sub, previous, current))
            # print(diff)
            if diff[0] != 0:
                step_x = -1 if previous[0] > current[0] else 1
                y = current[1]
                for x in range(previous[0], current[0]+ step_x, step_x):
                    filled_points[(x, y)] = 'w'
                    if y > lowest_point: lowest_point = y
                    print((x, y))
            if diff[1] != 0:
                step_y = -1 if previous[1] > current[1] else 1
                x = current[0]
                for y in range(previous[1], current[1]+ step_y, step_y):
                    filled_points[(x, y)] = 'w'
                    if y > lowest_point: lowest_point = y
                    print((x, y))
            previous = current
print(f'lowest point {lowest_point}')
floor_y = lowest_point + 2 # floor is 2 lower than lowest point
sand_start = (500, 0)
done = False
sand_grains = 0
while not done:
    if is_filled(*sand_start):
        done = True
        continue
    sand_grains += 1
    sand_stopped = False
    (x, y) = sand_start
    # print(f'sand at {(x,y)}')
    while not sand_stopped:

        # print('sand', x, y)
        if not is_filled(x, y+1):
            y += 1
        elif not is_filled(x-1, y+1):
            y += 1
            x -= 1
        elif not is_filled(x+1, y+1):
            y += 1
            x += 1
        else:
            filled_points[(x,y)] = 's'
            sand_stopped= True
            print('stopped', x,y)




print(f'Total grains before stopped: {sand_grains}')


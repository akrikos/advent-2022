import re
import operator

point_regex = re.compile('(\d+),(\d+)')

filled_points = {}
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
sand_start = (500, 0)
sand_falling_infinitely = False
sand_grains = 0
while not sand_falling_infinitely:
    sand_grains += 1
    sand_stopped = False
    (x, y) = sand_start
    # print(f'sand at {(x,y)}')
    while not sand_stopped:

        print('sand', x, y)
        if y >= lowest_point:
            print('falling infinitely')
            sand_stopped= True
            sand_falling_infinitely = True
        elif filled_points.get((x, y+1), None) is None:
            y += 1
        elif filled_points.get((x-1, y+1), None) is None:
            y += 1
            x -= 1
        elif filled_points.get((x+1, y+1), None) is None:
            y += 1
            x += 1
        else:
            filled_points[(x,y)] = 's'
            sand_stopped= True
            print('stopped', x,y)




print(f'Total grains before free flow: {sand_grains-1}')


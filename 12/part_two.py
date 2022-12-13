import operator
import sys
import queue

# sys.setrecursionlimit(15000)

# rules
# only step to max 1 letter difference on up, fall however far you want
# never a need to revisit a path
# done when can't move any more or at endpoint

# first algorithm try:
# move towards endpoint if possible
# depth-first and print out as we go
#
# find shortest path

# with open('test_input.txt') as file:
with open('input.txt') as file:
    grid = file.read().splitlines()

DIRECTIONS = {
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1)
}

def get_tiny_grid(x, y):
    tiny_grid = []
    for i in range (-2, 3):
        line = []
        tiny_grid.append(line)
        for j in range(-2, 3):
            line.append(get_grid_item(x+j, y+i))
    return tiny_grid

def get_grid_item(coord, grid):
    (x, y) = coord
    if x < 0 or x >= len(grid[0]) or \
        y < 0 or y >= len(grid):
        return None # yer off the edge
    return grid[y][x]

def get_height(c):
    if c == None:
        return 10000000
    if c == 'E':
        return ord('z')
    if c == 'S':
        return ord('a')
    return ord(c)


def is_valid_step(f, t, grid):
    return get_height(get_grid_item(t, grid)) - get_height(get_grid_item(f, grid)) <= 1


def stepsToGoal(grid, startLocation, endLocation):
    print(f'Start: {startLocation} End: {endLocation}')
    nodes_to_see = queue.PriorityQueue()
    nodes_to_see.put((0, startLocation))
    seen_nodes = set()

    while not nodes_to_see.empty():
        (steps, current_node) = nodes_to_see.get_nowait()
        # print(steps, current_node)
        # seen_nodes.add(current_node)
        if current_node == endLocation:
            return steps
        for direction in DIRECTIONS.values():
            possible_walk = tuple(map(operator.add, current_node, direction))
            if possible_walk not in seen_nodes and is_valid_step(current_node, possible_walk, grid):
                nodes_to_see.put((steps+1, possible_walk))
                seen_nodes.add(possible_walk)

startLocations = set()
endLocation = None
for y, row in enumerate(grid):
    for x in range(0, len(grid)):
        if get_height(get_grid_item((x, y), grid)) == get_height('a'):
            startLocations.add((x,y))
    if not endLocation:
        endColumn = row.find('E')
        if endColumn != -1:
            endLocation = (endColumn, y)

possible_steps = set()
for startLocation in startLocations:
    possible_steps.add(stepsToGoal(grid, startLocation, endLocation))

possible_steps.remove(None) # throw out unwalkable paths
print(f'Steps: {min(possible_steps)}')

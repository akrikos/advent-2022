import operator
import sys
import queue

# sys.setrecursionlimit(15000)

# rules
# only step to max 1 letter difference
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

startLocation = None
endLocation = None

# find start and end
for y, row in enumerate(grid):
    if not startLocation:
        startColumn = row.find('E')
        if startColumn != -1:
             startLocation = (startColumn, y )
    if not endLocation:
        endColumn = row.find('S')
        if endColumn != -1:
             endLocation = (endColumn, y)

print(f'Start: {startLocation} End: {endLocation}')


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

# lowest = 200
# max_visited_count = 200
# dead_nodes = set()
# absolute_visited = dict()
# search_count = 0
# possibleSteps = set()
# def recursiveSearch(current: tuple, visited: set):
#     global lowest
#     if get_height(get_grid_item(*current)) < lowest:
#         lowest = get_height(get_grid_item(*current))
#         print('lowest', get_grid_item(*current), current)
#     # if get_grid_item(*current) == 'p':
#     #     pass
#     global search_count
#     # if absolute_visited.get(current, 0) >= max_visited:
#     #     return
#     search_count += 1
#     # print(len(visited))
#     absolute_visited[current] = absolute_visited.get(current, 0) + 1

#     if search_count % 10000 == 0:
#         print(f'moving through ({current}), {search_count}')
#         pass
#     # print(f'visiting {current}')
#     visited.add(current)
#     if current == endLocation:
#         # visited start but didn't step to it, so -1
#         steps = len(visited) - 1
#         print(f'Finished! steps: {steps}')
#         possibleSteps.add(steps)
#         print(f'Current Min steps {min(possibleSteps)}')

#     # difference = tuple(map(operator.sub, current, endLocation))
#     possibleLocs = []
#     for name, locDiff in DIRECTIONS.items():
#         coord = tuple(map(operator.add, current, locDiff))
#         if coord in visited:
#             # print(f'already visited {coord}')
#             continue
#         if coord[0] < 0 or coord[0] >= len(grid[0]) or \
#             coord[1] < 0 or coord[1] >= len(grid):
#             # print(f'off map {coord}')
#             continue
#         nextItem = get_grid_item(*coord)
#         currentItem = get_grid_item(*current)
#         currenHeight = get_height(currentItem)
#         nextHeight = get_height(nextItem)
#         # if nextHeight - currenHeight > 1:
#         if currenHeight - nextHeight > 1: # backwards because moving from end to start
#             if currenHeight - nextHeight < 0:
#                 print('falling')
#             # print(f'no climbing {nextHeight - currenHeight}')
#             continue
#         possibleLocs.append(coord)

#     # for loc in possibleLocs:
#     #     recursiveSearch(loc, set(visited))

#     differences = []
#     for loc in possibleLocs:
#         # if absolute_visited.get(loc, 0) < max_visited_count:
#         difference = abs(loc[0] - endLocation[0]) + abs(loc[1] - endLocation[1])
#         differences.append((difference, loc))

#     differences.sort()
#     for _, loc in differences:
#         if loc not in dead_nodes:
#             recursiveSearch(loc, set(visited))

#     dead_nodes.add(current)

# recursiveSearch(startLocation, set())
# if len(possibleSteps) > 0:
#     print(f'Min steps {min(possibleSteps)}')
# else:
#     print('Sad Trombone')

def is_valid_step(f, t, grid):
    return get_height(get_grid_item(t, grid)) - get_height(get_grid_item(f, grid)) <= 1


def stepsToGoal(grid, startLocation, endLocation):
    nodes_to_see = queue.PriorityQueue()
    nodes_to_see.put((0, startLocation))
    seen_nodes = set()

    while not nodes_to_see.empty():
        (steps, current_node) = nodes_to_see.get_nowait()
        print(steps, current_node)
        # seen_nodes.add(current_node)
        if current_node == endLocation:
            return steps
        for direction in DIRECTIONS.values():
            possible_walk = tuple(map(operator.add, current_node, direction))
            if possible_walk not in seen_nodes and is_valid_step(current_node, possible_walk, grid):
                nodes_to_see.put((steps+1, possible_walk))
                seen_nodes.add(possible_walk)

startLocation = None
endLocation = None
for y, row in enumerate(grid):
    if not startLocation:
        startColumn = row.find('S')
        if startColumn != -1:
            startLocation = (startColumn, y )
    if not endLocation:
        endColumn = row.find('E')
        if endColumn != -1:
            endLocation = (endColumn, y)

print(f'Steps: {stepsToGoal(grid, startLocation, endLocation)}')
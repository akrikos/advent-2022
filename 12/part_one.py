import operator

# rules
# only step to max 1 letter difference
# never a need to revisit a path
# done when can't move any more or at endpoint

# first algorithm try:
# move towards endpoint if possible
# depth-first and print out as we go
#
# find shortest path

with open('test_input.txt') as file:
# with open('input.txt') as file:
    grid = file.read().splitlines()

startLocation = None
endLocation = None

# find start and end
for y, row in enumerate(grid):
    if not startLocation:
        startColumn = row.find('S')
        if startColumn != -1:
             startLocation = (startColumn, y )
    if not endLocation:
        endColumn = row.find('E')
        if endColumn != -1:
             endLocation = (endColumn, y)

print(f'Start: {startLocation} End: {endLocation}')


DIRECTIONS = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

def get_grid_item(x, y):
    return grid[y][x]


possibleSteps = set()
def recursiveSearch(current: tuple, visited: set):
    if len(visited) % 100 == 0:
        print(f'moving through ({current})')
        pass
    # print(f'visiting {current}')
    visited.add(current)
    if current == endLocation:
        # visited start but didn't step to it, so -1
        steps = len(visited) - 1
        print(f'Finished! steps: {steps}')
        possibleSteps.add(steps)
        print(f'Current Min steps {min(possibleSteps)}')

    # difference = tuple(map(operator.sub, current, endLocation))
    possibleLocs = []
    for name, locDiff in DIRECTIONS.items():
        coord = tuple(map(operator.add, current, locDiff))
        if coord in visited:
            # print(f'already visited {coord}')
            continue
        if coord[0] < 0 or coord[0] >= len(grid[0]) or \
            coord[1] < 0 or coord[1] >= len(grid):
            # print(f'off map {coord}')
            continue
        nextItem = get_grid_item(*coord)
        currentItem = get_grid_item(*current)
        currenHeight = ord('a') if currentItem == 'S' else ord(currentItem)
        nextHeight = ord('z') if nextItem == 'E' else ord(nextItem)
        if abs(nextHeight - currenHeight) > 1:
            # print(f'no climbing {nextHeight - currenHeight}')
            continue
        possibleLocs.append(coord)

    for loc in possibleLocs:
        recursiveSearch(loc, set(visited))

    # differences = []
    # for loc in possibleLocs:
    #     difference = abs(loc[0] - endLocation[0]) + abs(loc[1] - endLocation[1])
    #     differences.append((difference, loc))
    #     # ()
    # for _, loc in sorted(differences):
    #     recursiveSearch(loc, set(visited))

recursiveSearch(startLocation, set())

print(f'Min steps {min(possibleSteps)}')

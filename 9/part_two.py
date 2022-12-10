import re
from operator import add, sub

parse_regex = re.compile('(.) (\d+)')

DIRECTIONS = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

def next_tail_pos(leader_pos, follower_pos):
    differences = tuple(map(sub, leader_pos, follower_pos))
    tail_x_mod = 0
    tail_y_mod = 0
    if (abs(differences[0]) > 1 or abs(differences[1]) > 1):
        if (abs(differences[0]) != 0):
            if (differences[0] > 0):
                tail_x_mod = 1
                # tail_pos[0] += 1
            else:
                tail_x_mod = -1
                # tail_pos[0] -= 1
        if (abs(differences[1]) != 0):
            if (differences[1] > 0):
                tail_y_mod = 1
                # tail_pos[1] += 1
            else:
                tail_y_mod = -1
                # tail_pos[1] -= 1
    tail_pos = tuple(map(add, follower_pos, (tail_x_mod, tail_y_mod)))
    return tail_pos

# head_pos = (0, 0)
# tail_pos = (0, 0)
positions = [(0,0)]*10
visited = set()
# with open('test_input.txt', 'r') as file:
# with open('test_input_2.txt', 'r') as file:
with open('input.txt', 'r') as file:
    for line in file:
        # print('---')
        m = parse_regex.match(line)
        (direction, count) = m.groups()
        count = int(count)
        # print(direction, count)
        for i in range(count):
            positions[0] = tuple(map(add, positions[0], DIRECTIONS[direction]))
            # head_pos = tuple(map(add, head_pos, DIRECTIONS[direction]))
            for i in range(1, len(positions)):
                positions[i] = next_tail_pos(positions[i-1], positions[i])
            # tail_pos = next_tail_pos(head_pos, tail_pos)
            # print(f'new head {head_pos}, new tail {tail_pos}')
            visited.add(positions[-1])


print(f'Visited {len(visited)} spaces.')




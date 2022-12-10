import re
from operator import add, sub

parse_regex = re.compile('(.) (\d+)')

DIRECTIONS = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


head_pos = (0, 0)
tail_pos = (0, 0)
visited = set()
# with open('test_input.txt', 'r') as file:
with open('input.txt', 'r') as file:
    for line in file:
        print('---')
        m = parse_regex.match(line)
        (direction, count) = m.groups()
        count = int(count)
        # print(direction, count)
        for i in range(count):
            head_pos = tuple(map(add, head_pos, DIRECTIONS[direction]))
            differences = tuple(map(sub, head_pos, tail_pos))
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
            tail_pos = tuple(map(add, tail_pos, (tail_x_mod, tail_y_mod)))
            print(f'new head {head_pos}, new tail {tail_pos}')
            visited.add(tail_pos)


print(f'Visited {len(visited)} spaces.')




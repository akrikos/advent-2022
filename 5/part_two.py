import re

from collections import deque

stacks = []
named_stacks = {}
finished_initial_state = False

num_stacks = 9
# num_stacks = 3

for i in range(num_stacks):
    stacks.append([])

move_regex = re.compile('move ([0-9]+) from ([0-9]+) to ([0-9]+)')
def perform_move(line):
    m = move_regex.match(line)
    (num_to_move, from_col, to_col) = m.groups()
    print(num_to_move, from_col, to_col)
    int_to_move = int(num_to_move)
    crates_to_move = named_stacks[from_col][0:int_to_move]
    named_stacks[from_col] = named_stacks[from_col][int_to_move:]
    named_stacks[to_col] = crates_to_move + named_stacks[to_col]
    # for i in range(int(num_to_move)):
    #     crate = named_stacks[from_col].popleft()
    # named_stacks[to_col].appendleft(crate)

with open('input.txt', 'r') as file:
# with open('test_input.txt', 'r') as file:
    for line in file:
        if not finished_initial_state:
            if '[' in line:
                for i in range(num_stacks):
                    next_index = 3*i+i+1
                    if next_index > len(line):
                        continue
                    crate = line[next_index]
                    if crate != ' ':
                        stacks[i].append(crate)
            else:
                line = line.strip()
                names = re.split(' +', line)
                for i, name in enumerate(names):
                    if name == '':
                        continue
                    named_stacks[name] = stacks[i]
                finished_initial_state = True
                print(named_stacks)
        elif line == '\n':
            print('init done')
        else:
            perform_move(line)
output = ''
for i in range(1, num_stacks + 1):
    output += named_stacks[chr(ord('0')+i)][0]

print(output)

import re

from collections import deque

stacks = []
named_stacks = {}
finished_initial_state = False

for i in range(9):
    stacks.append(deque())

move_regex = re.compile('move ([0-9]+) from ([0-9]+) to ([0-9]+)')
def perform_move(line):
    m = move_regex.match(line)
    (num_to_move, from_col, to_col) = m.groups()
    print(num_to_move, from_col, to_col)
    for i in range(int(num_to_move)):
        crate = named_stacks[from_col].popleft()
        named_stacks[to_col].appendleft(crate)

with open('input.txt', 'r') as file:
    for line in file:
        if not finished_initial_state:
            if line[0] != ' ':
                for i in range(9):
                    crate = line[3*i+i+1]
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
for stack in stacks:
    output += stack[0]

print(output)

import re
import math
import operator

items_regex = re.compile("  Starting items: (.+)")
operation_regex = re.compile("  Operation: new = old (.) (.+)")
test_regex = re.compile("  Test: divisible by (\d+)")
destination_regex = re.compile(".*If .+: throw to monkey (\d+)")

class Monkey:
    def getOperation(line):
        m = operation_regex.match(line)
        (operator_str, operand) = m.groups()
        if (operator_str == '+'):
            operator_func = operator.add
        elif (operator_str == '*'):
            operator_func = operator.mul

        if operand == 'old':
            return lambda old: operator_func(old, old)
        else:
            return lambda old: operator_func(old, int(operand))

    def __init__(self, text_input):
        lines = text_input.split('\n')
        self.name = lines[0][7]
        self.items = list(map(int, items_regex.match(lines[1]).group(1).split(', ')))
        self.operation = Monkey.getOperation(lines[2])
        self.test_num = int(test_regex.match(lines[3]).group(1))
        self.trueDestination = int(destination_regex.match(lines[4]).group(1))
        self.falseDestination = int(destination_regex.match(lines[5]).group(1))
        self.num_inspections = 0

    def test(self, item):
        return item % self.test_num == 0

    def inspect(self, item):
        self.num_inspections += 1
        return self.operation(item)

    def __str__(self):
        return f'Name: {self.name}; Items: {self.items}'

    def __lt__(self, other):
        return self.num_inspections < other.num_inspections

monkies = []
# with open('test_input.txt') as file:
with open('input.txt') as file:
    monkey_blocks = file.read().split('\n\n')
    for block in monkey_blocks:
        monkies.append(Monkey(block))

    # find least common multiple to keep things bounded
    lcm = 1
    # lcm = functools.reduce(operator.mul, [m.test_num for m in monkies], 1)
    for monkey in monkies:
        lcm = lcm * monkey.test_num

    print(f'Initial---')
    for i, monkey in enumerate(monkies):
        print(f'Monkey {i}: {monkey}')

    for round in range(10000):
        for monkey in monkies:
            for worry_level_item in monkey.items:
                new_level_item = monkey.inspect(worry_level_item)
                # got to keep things bounded;
                bored_item_level = new_level_item % lcm

                if monkey.test(bored_item_level):
                    monkies[monkey.trueDestination].items.append(bored_item_level)
                else:
                    monkies[monkey.falseDestination].items.append(bored_item_level)
            monkey.items = []
        if (round % 1000 == 0):
            print(f'Round({round})---')
            for i, monkey in enumerate(monkies):
                print(f'Monkey {i}: {monkey}')


print(f'Inspections---')
for i, monkey in enumerate(monkies):
    print(f'Monkey {i}: {monkey.num_inspections}')

monkies.sort(reverse = True)
print(f'2 top monkies: {monkies[0].name} with i={monkies[0].num_inspections} and {monkies[1].name} with i={monkies[1].num_inspections}')
print(f'Monkey Business is {monkies[0].num_inspections*monkies[1].num_inspections}')

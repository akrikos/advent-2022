class weird_cpu:
    noop_name = 'noop'
    addx_name = 'addx'

    def __init__(self):
        self.cycle_values = [1]
        self.instructions = []

    def append_instruction(self, instruction_name, value=0):
        self.instructions.append([instruction_name, value])

    def run_instructions(self):
        for instruction in self.instructions:
            if instruction[0] == weird_cpu.noop_name:
                self.noop()
            elif instruction[0] == weird_cpu.addx_name:
                self.addx(instruction[1])

    def noop(self):
        self.cycle_values.append(self.cycle_values[-1])

    def addx(self, value):
        self.cycle_values.append(self.cycle_values[-1])
        self.cycle_values.append(self.cycle_values[-1] + int(value))

    def get_cycle_value(self, number):
        # returns numberth value
        # 20th value is the 19th index because index starts with 0
        if number > len(self.cycle_values)                :
            print('warning: after total cycles')
            return self.cycle_values[-1]
        return self.cycle_values[number - 1]




cpu = weird_cpu()

# with open('test_input_1.txt') as file:
# with open('test_input_2.txt') as file:
with open('input.txt') as file:
    for line in file:
        cpu.append_instruction(*line.strip().split(' '))
    cpu.run_instructions()
    signal_strengths = []
    for i in range(20, len(cpu.cycle_values), 40):
        print(f'cycle value for cycle {i} is {cpu.get_cycle_value(i)}')
        signal_strengths.append(i*cpu.get_cycle_value(i))
    print(signal_strengths)
    print(f'Sum of signal strengths {sum(signal_strengths)}')

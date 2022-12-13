import collections
import re

class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.correct = self.is_correct()

    def is_correct():
        pass

def parse_list(text):
    list_stack = collections.deque()
    result = None
    number_text = ''
    for char in text:
        if re.match('\d', char) is not None:
            number_text += char
            continue
        elif len(number_text) > 0:
            list_stack[0].append(int(number_text))
            number_text = ''

        if char == ' ' or char == ',':
            continue
        elif char == '[':
            list = []
            if not result:
                result = list
            else:
                list_stack[0].append(list)
            list_stack.appendleft(list)
        elif char == ']':
            list_stack.popleft()
    return result

def parse_pairs(input_text):
    pairs = []
    for pair_text in input_text.split('\n\n'):
        (left_text, right_text) = pair_text.split('\n')
        pairs.append(Pair(parse_list(left_text)), Pair(parse_list(right_text)))


print(parse_list('[1,[2,[3,[4,[5,6,7]]]],8,9]'))

# input = ''
# with open('test_input.txt') as file:
#     input = file.read()

# pairs = parse_pairs(input)
# sum_correct_indices = 0
# for i, pair in enumerate(pairs):
#     if pair.correct:
#         sum_correct_indices += (1+i) # 1 based index

# print(f'Sum of correctly ordered indices: {sum_correct_indices}')

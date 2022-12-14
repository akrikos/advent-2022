import collections
import re
import functools

class Pair:
    def cmp_lists(left, right):
        # returns 0 if ==, < 0 if left is lower, > 0 if left is higher

        if isinstance(left, int) and isinstance(right, int):
            return left - right

        if isinstance(left, list) and isinstance(right, list):
            for (l, r) in zip(left, right):
                val = Pair.cmp_lists(l, r)
                if val != 0:
                    return val
            return len(left) - len(right)
        elif isinstance(left, int):
            return Pair.cmp_lists([left], right)
        else:
            return Pair.cmp_lists(left, [right])

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.correct = self.is_correct()

    def is_correct(self):
        return Pair.cmp_lists(self.left, self.right) < 1



def parse_lists(text):
    # apparently JSON.loads() works too
    return eval(text)

def get_lists(input_text):
    lists = []
    for pair_text in input_text.split('\n\n'):
        (left_text, right_text) = pair_text.split('\n')
        lists.append(parse_lists(left_text))
        lists.append(parse_lists(right_text))
    return lists


# print(parse_lists('[1,[2,[3,[4,[5,6,7]]]],8,9]'))
# p = parse_pairs("[9]\n[[8,7,6]]")
# p = parse_pairs("[[[]]]\n[[]]")
# p = parse_pairs("[8,1,8,7]\n[8,1,8,7,0]")
# p = parse_pairs("[[],[4,[],0,[],6],[[[5],[4,3,6]],[[7,6],5],[[3,9],2],7],[4,[],2,[3,[],10]]]\n[[[0,2],[6,[5,9,8],[1,8,1]]],[[[1,3,0],[],0,10],[6],3],[[[1,1,6,2,1]],9],[[[5,0,4],5,[1,2,5,10,2]],[[7,8,4],1]]]")
# print(p[0].correct)

input = ''
# with open('test_input.txt') as file:
with open('input.txt') as file:
    input = file.read()
divider_packets = [
    [[2]],
    [[6]]
]
lists = get_lists(input)
lists += divider_packets
lists.sort(key=functools.cmp_to_key(Pair.cmp_lists))

for i, list in enumerate(lists):
    print(i, list)

key = (lists.index(divider_packets[0]) + 1) * (lists.index(divider_packets[1]) + 1)
print(f'Decoder key: {key}')
# print(f'Sum of correctly ordered indices: {sum_correct_indices}')

# 3411 is too low
# 5450 is too low

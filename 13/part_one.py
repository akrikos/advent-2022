import collections
import re

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



        # # edge case, left is an empty list - but that would have returned 0 which is still true, so this doesn't matter
        # # except this found a bunch more, so maybe this did matter????? 3411-5450
        # if type(left) == list and len(left) == 0 and (type(right) == int or (type(right) == list and len(right) > 0)):
        #     return -1
        # for i, left_item in enumerate(left):
        #     # right list is too short
        #     try:
        #         right_item = right[i]
        #     except:
        #         return 1

        #     cmp = None
        #     if type(left_item) == int and type(right_item) == int:
        #         cmp = left_item - right_item
        #     elif type(left_item) == list and type(right_item) == list:
        #         cmp = Pair.cmp_lists(left_item, right_item)
        #     elif type(left_item) == list:
        #         cmp = Pair.cmp_lists(left_item, [right_item])
        #     elif type(right_item) == list:
        #         cmp = Pair.cmp_lists([left_item], right_item)

        #     if cmp is None:
        #         print('yer broke')

        #     if cmp != 0:
        #         return cmp

        # return 0

    # def cmp_lists(a, b):
    #     if isinstance(a, list) and isinstance(b, list):
    #         for x, y in zip(a, b):
    #             if (val := Pair.cmp_lists(x, y)) != 0:
    #                 return val
    #             return Pair.cmp_lists(len(a), len(b))
    #     elif isinstance(a, list):
    #         return Pair.cmp_lists(a, [b])
    #     elif isinstance(b, list):
    #         return Pair.cmp_lists([a], b)
    #     else:
    #         return (a > b)-(a < b)

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.correct = self.is_correct()

    def is_correct(self):
        return Pair.cmp_lists(self.left, self.right) < 1



def parse_lists(text):
    # apparently JSON.loads() works too
    return eval(text)
    # list_stack = collections.deque()
    # result = None
    # number_text = ''
    # for char in text:
    #     if re.match('\d', char) is not None:
    #         number_text += char
    #         continue
    #     elif len(number_text) > 0:
    #         list_stack[0].append(int(number_text))
    #         number_text = ''

    #     if char == ' ' or char == ',':
    #         continue
    #     elif char == '[':
    #         list = []
    #         if result is None:
    #             result = list
    #         else:
    #             list_stack[0].append(list)
    #         list_stack.appendleft(list)
    #     elif char == ']':
    #         list_stack.popleft()
    # return result

def parse_pairs(input_text):
    pairs = []
    for pair_text in input_text.split('\n\n'):
        (left_text, right_text) = pair_text.split('\n')
        pairs.append(Pair(parse_lists(left_text), parse_lists(right_text)))
    return pairs


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

pairs = parse_pairs(input)
sum_correct_indices = 0
for i, pair in enumerate(pairs):
    # print(i, pair.correct, pair.left, pair.right)
    if pair.correct:
        sum_correct_indices += (1+i) # 1 based index

print(f'Sum of correctly ordered indices: {sum_correct_indices}')

# 3411 is too low
# 5450 is too low

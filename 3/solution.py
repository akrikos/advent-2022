
def find_common_letter(first: str, second: str) -> str:
    for letter in first:
        if letter in second:
            return letter
    raise Exception('no common letter found')

def calc_priority(letter: str) -> int:
    if letter >= 'A' and letter <= 'Z':
        return ord(letter) - ord('A') + 27
    return ord(letter) - ord('a') + 1

total = 0
with open('input.txt', 'r') as file:
    for line in file:
        # remove \n
        line = line[:-1]
        length = len(line)
        first_half = line[0:int(length/2)]
        second_half = line[int(length/2):]
        common_letter = find_common_letter(first_half, second_half)
        priority = calc_priority(common_letter)
        total += priority

print(total)


def find_common_letter(lines: list) -> str:
    for letter in lines[0]:
        if letter in lines[1] and letter in lines[2]:
            return letter
    raise Exception('no common letter found')

def calc_priority(letter: str) -> int:
    if letter >= 'A' and letter <= 'Z':
        return ord(letter) - ord('A') + 27
    return ord(letter) - ord('a') + 1

total = 0
group_counter = 0
group_lines = []
with open('input.txt', 'r') as file:
    for line in file:
        group_counter += 1
        # remove \n
        line = line[:-1]
        group_lines.append(line)
        if (group_counter == 3):
            group_counter = 0
            common_letter = find_common_letter(group_lines)
            group_lines = []
            priority = calc_priority(common_letter)
            total += priority

print(total)
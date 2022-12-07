# part one
# num_unique_chars = 4
# part two
num_unique_chars = 14

def is_all_unique(x:list) -> bool:
    for i in x:
        if x.count(i) > 1:
            return False
    return True

def find_first_unique_index(input):
    last_x_chars = []
    for index, char in enumerate(input):
        if len(last_x_chars) == num_unique_chars:
            if is_all_unique(last_x_chars):
                return index
            last_x_chars = last_x_chars[1:]
            last_x_chars.append(char)
        else:
            last_x_chars.append(char)
    return -1


first_index = -1
with open('input.txt', 'r') as file:
# input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    input = file.readline().strip()
    first_index = find_first_unique_index(input)

print(first_index)



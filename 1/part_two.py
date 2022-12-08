from collections import deque
# calories each elf is carrying is input

num_to_keep = 3
def keep_highest(new: int, highest: deque) -> deque:
    # highest always stays sorted so that first element is largest
    if len(highest) < num_to_keep:
        highest.append(new)
        return sorted(highest, reverse=True)
    if new > highest[-1]:
        for index, item in enumerate(highest):
            if new > item:
                highest.insert(index, new)
                if len(highest) > num_to_keep:
                    highest.pop()
                return highest

    return highest;


with open('input.txt', 'r') as file:
    most_calories = deque()
    current_calories = 0
    for line in file:
        if line == "\n":
            # reset for new elf
            most_calories = keep_highest(current_calories, most_calories)
            current_calories = 0
        else:
            current_calories += int(line)

    # print(most_calories)
    print(sum(most_calories))
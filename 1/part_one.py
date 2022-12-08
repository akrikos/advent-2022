from collections import deque
# calories each elf is carrying is input

with open('input.txt', 'r') as file:
    most_calories = 0
    current_calories = 0
    for line in file:
        if line == "\n":
            # reset for new elf
            # most_calories = keep_highest(current_calories, most_calories)
            if current_calories > most_calories:
                most_calories = current_calories
            current_calories = 0
        else:
            current_calories += int(line)

    print(most_calories)
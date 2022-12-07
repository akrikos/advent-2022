from collections import deque

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'Z': 6,
    'Y': 3,
    'X': 0
}

# they play key, I play value
win_dict = {'A': 'B', 'B': 'C', 'C': 'A'}

lose_dict = {'A': 'C', 'B': 'A', 'C': 'B'}

def get_action(opponent_move: str, outcome: str) -> str:

    # lose
    if outcome == 'X':
        return lose_dict[opponent_move]
    # tie
    if outcome == 'Y':
        return opponent_move
    #win
    return win_dict[opponent_move]


def get_score(outcome, my_action):
    return scores[outcome] + scores[my_action]

total = 0
with open('input.txt', 'r') as file:
    for line in file:
        opponent_action = line[0]
        needed_outcome = line[2]
        my_action = get_action(opponent_action, needed_outcome)
        score = get_score(needed_outcome, my_action)
        total += score

print(total)
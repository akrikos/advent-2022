move_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'win': 6,
    'tie': 3,
    'lose': 0
}

def get_outcome(opponent_action, my_action):
    opponent_num = ord(opponent_action)
    my_num = ord(my_action) - 23
    if (opponent_num == my_num):
        return move_scores['tie']
    difference = opponent_num - my_num
    if difference == 1 or difference == -2:
        return move_scores['lose']
    return move_scores['win']

def get_score(outcome, my_action):
    return outcome + ord(my_action) - ord('A') - 22

total = 0
with open('input.txt', 'r') as file:
    for line in file:
        opponent_action = line[0]
        my_action = line[2]
        outcome = get_outcome(opponent_action, my_action)
        total += get_score(outcome, my_action)

print (total)
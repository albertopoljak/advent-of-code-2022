ROCK_ENEMY, PAPER_ENEMY, SCISSORS_ENEMY = "A", "B", "C"
ROCK_PLAYER, PAPER_PLAYER, SCISSORS_PLAYER = "X", "Y", "Z"


def get_player_hand_score(player_hand_symbol: str) -> int:
    if player_hand_symbol == ROCK_PLAYER:
        return 1
    elif player_hand_symbol == PAPER_PLAYER:
        return 2
    elif player_hand_symbol == SCISSORS_PLAYER:
        return 3

    return 0


SCORE_LOSS = 0
SCORE_DRAW = 3
SCORE_WIN = 6


with open("input1.txt") as f:
    data = tuple(line.split() for line in f.readlines())

total_score = 0


for play in data:
    enemy_hand, player_hand = play
    total_score += get_player_hand_score(player_hand)

    if player_hand == ROCK_PLAYER:
        if enemy_hand == ROCK_ENEMY:
            total_score += SCORE_DRAW
        elif enemy_hand == PAPER_ENEMY:
            total_score += SCORE_LOSS
        elif enemy_hand == SCISSORS_ENEMY:
            total_score += SCORE_WIN

    elif player_hand == PAPER_PLAYER:
        if enemy_hand == ROCK_ENEMY:
            total_score += SCORE_WIN
        elif enemy_hand == PAPER_ENEMY:
            total_score += SCORE_DRAW
        elif enemy_hand == SCISSORS_ENEMY:
            total_score += SCORE_LOSS

    elif player_hand == SCISSORS_PLAYER:
        if enemy_hand == ROCK_ENEMY:
            total_score += SCORE_LOSS
        elif enemy_hand == PAPER_ENEMY:
            total_score += SCORE_WIN
        elif enemy_hand == SCISSORS_ENEMY:
            total_score += SCORE_DRAW


print(total_score)

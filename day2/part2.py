ROCK_ENEMY, PAPER_ENEMY, SCISSORS_ENEMY = "A", "B", "C"
SYMBOL_LOSE, SYMBOL_DRAW, SYMBOL_WIN = "X", "Y", "Z"

SCORE_ROCK = 1
SCORE_PAPER = 2
SCORE_SCISSORS = 3

SCORE_LOSS = 0
SCORE_DRAW = 3
SCORE_WIN = 6


with open("input1.txt") as f:
    data = tuple(line.split() for line in f.readlines())

total_score = 0


for play in data:
    enemy_hand, round_expectation = play

    if round_expectation == SYMBOL_LOSE:
        total_score += SCORE_LOSS
        if enemy_hand == ROCK_ENEMY:
            total_score += SCORE_SCISSORS
        elif enemy_hand == PAPER_ENEMY:
            total_score += SCORE_ROCK
        elif enemy_hand == SCISSORS_ENEMY:
            total_score += SCORE_PAPER

    elif round_expectation == SYMBOL_DRAW:
        total_score += SCORE_DRAW
        if enemy_hand == ROCK_ENEMY:
            total_score += SCORE_ROCK
        elif enemy_hand == PAPER_ENEMY:
            total_score += SCORE_PAPER
        elif enemy_hand == SCISSORS_ENEMY:
            total_score += SCORE_SCISSORS

    elif round_expectation == SYMBOL_WIN:
        total_score += SCORE_WIN
        if enemy_hand == ROCK_ENEMY:
            total_score += SCORE_PAPER
        elif enemy_hand == PAPER_ENEMY:
            total_score += SCORE_SCISSORS
        elif enemy_hand == SCISSORS_ENEMY:
            total_score += SCORE_ROCK

print(total_score)

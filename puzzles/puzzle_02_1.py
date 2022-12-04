FILE_NAME = "input_03.txt"

with open(FILE_NAME) as f:
    data = f.read()

play_scores = {
    "r": 1,
    "p": 2,
    "s": 3}

game_scores = {
    "win": 6,
    "draw": 3,
    "loss": 0}

strategy_mapping = {
    "A": "r",
    "B": "p",
    "C": "s",
    "X": "r",
    "Y": "p",
    "Z": "s"}

game_outcomes = {
    "rr": "draw",
    "rp": "win",
    "rs": "loss",
    "pr": "loss",
    "pp": "draw",
    "ps": "win",
    "sr": "win",
    "sp": "loss",
    "ss": "draw"}

def get_game(a, b):
    game = strategy_mapping[a] + strategy_mapping[b]
    return game_outcomes[game]

def read_game(line):
    a = line[0]
    b = line[2]
    return (a, b)

score_sum = 0

for line in data.splitlines():
    a, b = read_game(line)
    game_outcome = get_game(a, b)
    score = game_scores[game_outcome] + play_scores[strategy_mapping[b]]
    print(f"Game {a} {b} : {game_outcome} and score {score}")
    score_sum += score

print(f"Total game score is {score_sum}")








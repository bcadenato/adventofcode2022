FILE_NAME = "input_03.txt"

with open(FILE_NAME) as f:
    data = f.read()

play_scores = {
    "r": 1,
    "p": 2,
    "s": 3
}

game_scores = {
    "w": 6,
    "d": 3,
    "l": 0
}

strategy_mapping = {
    "A": "r",
    "B": "p",
    "C": "s",
    "X": "l",
    "Y": "d",
    "Z": "w"
}

game_outcomes = {
    "rr": "draw",
    "rp": "win",
    "rs": "loss",
    "pr": "loss",
    "pp": "draw",
    "ps": "win",
    "sr": "win",
    "sp": "loss",
    "ss": "draw"
}

game_strategy = {
    "rw": "p",
    "rl": "s",
    "rd": "r",
    "pw": "s",
    "pl": "r",
    "pd": "p",
    "sw": "r",
    "sl": "p",
    "sd": "s"
}

def get_game(a, b):
    game = strategy_mapping[a] + strategy_mapping[b]
    return game_strategy[game]

def read_game(line):
    a = line[0]
    b = line[2]
    return (a, b)

score_sum = 0

# data = "A Y\nB X\nC Z\n"

for line in data.splitlines():
    a, b = read_game(line)
    game_play = get_game(a, b)
    score = game_scores[strategy_mapping[b]] + play_scores[game_play]
    print(f"Game {a} {b} : Need to play {game_play} for a score of {score}")
    score_sum += score

print(f"Total game score is {score_sum}")








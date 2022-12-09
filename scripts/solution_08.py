import puzzles.puzzle_08 as puzzle

FILE_INPUT = "puzzles/input_08.txt"

with open(FILE_INPUT) as f:
    forest_raw = f.read()

forest = puzzle.map_forest(forest_raw)

# Part 1

print(f'Visible trees in problem is {puzzle.count_visible(forest)}')

# Part 2

puzzle.calc_forest_score(forest)

problem_tree, problem_score = puzzle.find_max_score(forest)

print(f'Tree {problem_tree} has max score {problem_score}')


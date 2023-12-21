from itertools import combinations

# Define the length of the strip and the number of strokes
strip_length = 8
strokes = 3

#Each stroke paints a number of neighboring cells. In this question, it is specified as 2, so each stroke effectively covers 2 squares.
cells_covered_per_stroke = 2

# Total cells covered by all strokes
total_cells_covered = cells_covered_per_stroke * strokes

# Generate all possible combinations of starting positions for the strokes
# Since each stroke covers a specific number of neighboring cells, the starting position of each stroke must fall within the range of [0, strip_length - cells_covered_per_stroke]
possible_starts = range(strip_length - cells_covered_per_stroke + 1)

# Generate combinations of starting positions for the strokes
combinations_of_starts = list(combinations(possible_starts, strokes))
print(combinations_of_starts)
# Filter out invalid combinations where strokes overlap
valid_combinations = []
for combination in combinations_of_starts:
    valid = True
    for i in range(len(combination) - 1):
        # Check if the current stroke overlaps with the next one
        if combination[i] + cells_covered_per_stroke > combination[i + 1]:
            valid = False
            break
    if valid:
        valid_combinations.append(combination)

# The number of valid combinations is the answer
num_valid_combinations = len(valid_combinations)
print(num_valid_combinations)

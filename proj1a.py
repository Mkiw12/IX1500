import itertools

# Step 1: calculate number of U and L moves
n = 7 # total number of moves
k = 3
U_move = k
L_move = n - k
count = 0

# Step 2: create list of moves

moves = ['L'] * L_move + ['U'] * U_move

# Generate all unique permutaions of the moves
unique_paths = set(itertools.permutations(moves))


for path in unique_paths:
    count += 1
    print(''.join(path))

print("Total number of paths:", count)

import itertools

# All permuations of 3 'U' and 4 'L'

move = 'UUULLLL'

unique_paths = set(itertools.permutations(move))

valid_paths = []




# Check each path for validity
for path in unique_paths:
    y = 3  # Start y-coordinate
    valid = False  # Assume the path is invalid initially

    for move in path:
        if move == 'U':
            y += 1
        else:  # move == 'L'
            y -= 1

        # If the y-coordinate goes below or touches the x-axis
        if y <= 0:
            valid = True
            break  # No need to check further for this path

    if valid:
        valid_paths.append(''.join(path))

# Print all valid paths
for valid_path in valid_paths:
    print(valid_path)

print("Valid paths:",len(valid_path))
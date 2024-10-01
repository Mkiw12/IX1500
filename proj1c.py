from itertools import permutations
# Generate all permutations of 3 'U' and 4 'L'
all_paths = set(permutations('UUULLLL'))
valid_paths = []
# Check each path
for path in all_paths:
    y = 3  # starting y-coordinate
    is_valid = True
    for move in path:
        if move == 'U':
            y += 1
        else:  # move == 'L'
            y -= 1
        
        if y <= 0:  # if at any point y <= 0, it touches or crosses the x-axis
            is_valid = False
            break
    
    if is_valid:
        valid_paths.append(''.join(path))
print(f"Number of valid paths: {len(valid_paths)}")
print("Valid paths:")
for path in valid_paths:
    print(path)


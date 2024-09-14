from itertools import permutations

# Generate all permutations of 3 'U' and 4 'L'
all_paths = set(permutations('UUULLLL'))

valid_paths = []

# Function to print the diagram for a given path
def print_path_diagram(path):
    y = 3  # starting y-coordinate
    diagram = [' ' * y + 'S']  # Start point at y=3, marked with 'S'
    
    for move in path:
        if move == 'U':
            y += 1
        else:  # move == 'L'
            y -= 1
        diagram.append(' ' * y + '|')  # Move represented by '|'
    
    # Print the diagram
    print("Path diagram:")
    for line in diagram:
        print(line)
    print("\n")


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
        print(f"Valid path: {''.join(path)}")
        print_path_diagram(path)

print(f"\nNumber of valid paths: {len(valid_paths)}")



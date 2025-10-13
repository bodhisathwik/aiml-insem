
def function(x):
    return -x**2 + 4*x

def hill_climbing(start, step_size=0.1, max_iterations=100):
    current_x = start
    current_y = function(current_x)
    
    print(f"Starting Hill Climbing at x = {current_x:.2f}, f(x) = {current_y:.2f}")
    
    for i in range(max_iterations):
        # Generate neighbouring positions
        neighbours = [current_x + step_size, current_x - step_size]
        neighbours_values = [function(n) for n in neighbours]
        
        # Select the neighbour with the highest value
        max_neighbour_value = max(neighbours_values)
        max_neighbour = neighbours[neighbours_values.index(max_neighbour_value)]
        
        print(f"\nIteration {i + 1}:")
        print(f"Current position: x = {current_x:.2f}, f(x) = {current_y:.2f}")
        print(f"Neighbours: {[(n, function(n)) for n in neighbours]}")
        
        # Move if improvement
        if max_neighbour_value > current_y:
            current_x = max_neighbour
            current_y = max_neighbour_value
        else:
            print("Reached a peak. Stopping search.")
            break
    
    print(f"\nBest solution: x = {current_x:.2f}, f(x) = {current_y:.2f}")

hill_climbing(start=0.0)

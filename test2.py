import numpy as np

def generate_matrix_with_path(rows, cols):
    # Initialize matrix with all ones
    matrix = np.ones((rows, cols), dtype=int)
    
    # Choose a random starting row index
    start_row_index = np.random.randint(0, rows)
    
    # Set the starting column index to 0
    start_col_index = 0
    
    # Define the length of the path
    length = np.random.randint(1, cols)
    
    # Add continuous path of zeros
    for i in range(length):
        # Set the current position to zero
        matrix[start_row_index, start_col_index + i] = 0
    
    return matrix

# Define matrix dimensions
rows = 5
cols = 10

# Generate matrix with path of zeros
matrix_with_path = generate_matrix_with_path(rows, cols)

# Print matrix with continuous path of zeros
print(matrix_with_path)

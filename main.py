# Define the function below to compute the determinant of a 2 by 2 matrix.
def det2(matrix):
    '''
    Matrix takes a 2D list and computes the determinant before returning the value.
    @param matrix: 2D list of numeric data
    @return: float representing the determinant
    '''
    pass    

# Define the function below to compute the determinant of a 3 by 3 matrix
def det3(matrix):
    '''
    Matrix takes a 2D list and computes the determinant before returning the value.
    @param matrix: 2D list of numeric data
    @return: float representing the determinant
    '''
    pass    

def get_matrix():
    # Get rows and columns from user
    rows = int(input("Enter the number of rows and columns: "))
    columns = rows

    # Create empty list to store matrix values
    matrix = []

    # Iterate over rows and columns to fill matrix
    for r in range(rows):
        # Create empty list to store each row
        row_list = []
        for c in range(columns):
            # Get the value for the matrix position and append it to the row
            value = int(input(f"Enter the value for element {r+1}, {c+1}: "))
            row_list.append(value)
        
        # Append entire row to matrix
        matrix.append(row_list)
    
    # Return matrix
    return matrix

def main():
    '''
    Main function for the program.
    '''
    matrix = get_matrix()
    inverse = []

    # Determine size
    if len(matrix) == 2:
        inverse = det2(matrix)
    elif len(matrix) == 3:
        inverse = det2(matrix)
    else:
        print("The matrix's determinant cannot be computed.")

    print(inverse)


if __name__ == "__main__":
    main()

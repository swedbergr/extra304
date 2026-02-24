# Define the function below to compute product of two matrices using rank 1 matrices.
def multiplyR1(matrix1, matrix2):
    '''
    Matrix takes a two 2D lists and computes the produt before returning the product matrix
    as a 2D list. The product is computed using rank 1 matrices.
    @param matrix1: 2D list of numeric data
    @param matrix2: 2D list of numeric data
    @return: 2D list representing the product matrix
    '''
    pass      

def get_matrix():
    # Get rows and columns from user
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

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
    matrix1 = get_matrix()
    matrix2 = get_matrix()

    product = multiplyR1(matrix1, matrix2)

    print(product)


if __name__ == "__main__":
    main()

def multiply_matrices(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if multiplication is possible (cols of matrix1 == rows of matrix2)
    if cols_matrix1 != rows_matrix2:
        raise ValueError("Cannot multiply: Number of columns in matrix1 must equal number of rows in matrix2")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Perform multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = multiply_matrices(matrix1, matrix2)

print("Resultant Matrix:")
for row in result:
    print(row)

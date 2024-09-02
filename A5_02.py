rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))
rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))
matrix1 = []
matrix2 = []
print("Enter the elements of matrix 1:")
for i in range(rows1):
    row = []
    for j in range(cols1):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix1.append(row)
print("Enter the elements of matrix 2:")
for i in range(rows2):
    row = []
    for j in range(cols2):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix2.append(row)
if cols1 != rows2:
    print("Error: The number of columns in matrix 1 must be equal to the number of rows in matrix 2.")
else:
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            element = 0
            for k in range(cols1):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    print("Result:")
    for row in result:
        print(row)
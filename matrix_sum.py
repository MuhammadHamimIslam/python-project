def takeInp(row, col): 
    result = []
    for i in range(row): 
        rows = []
        for j in range(col):
            inp = int(input(f"Enter the value in {i}×{j}: "))
            rows.append(inp)
        result.append(rows)
    return result

def sumMatrix(m1, m2):
    if len(m1) != len(m2): 
        return "To perform matrix sum, Both length should be equal."
    result = []
    for i in range(len(m1)):
        rows = []
        for j in range(len(m1[0])): 
            rows.append(m1[i][j] + m2[i][j])
        result.append(rows)
    print(result)
    return result

def subsMatrix(m1, m2):
    if len(m1) != len(m2): 
        return "To perform matrix sum, Both length should be equal."
    result = []
    for i in range(len(m1)):
        rows = []
        for j in range(len(m1[0])): 
            rows.append(m1[i][j] - m2[i][j])
        result.append(rows)
    print(result)
    return result

def matrixOperation(matrix1, matrix2): 
    inp = input("Enter the operator: ")
    if inp == "+": 
        sumMatrix(matrix1, matrix2)
    elif inp == "-":
        subsMatrix(matrix1, matrix2)
        pass
    else:
        return "Invalid operator"

row = int(input("Enter the row number: ")) 
col = int(input("Enter the column number: "))

if row == 0: 
    print("Length can't be zero!")
elif col == 0:
    print("Length can't be zero!")    
else:
    print("Enter Value for matrix 1")    
    matrix1 = takeInp(row, col)
    print("Enter Value for matrix 2")
    matrix2 = takeInp(row, col)

    matrixOperation(matrix1, matrix2) 
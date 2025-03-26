def takeInp():
    row = int(input("Enter the row number: ")) 
    col = int(input("Enter the column number: "))
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
    if len(m1[0]) != len(m2[0]): 
        return  "To perform matrix sum, Both length should be equal."
    result = []
    for i in range(len(m1)):
        rows = []
        for j in range(len(m1[0])): 
            rows.append(m1[i][j] + m2[i][j])
        result.append(rows)
    return result

def subsMatrix(m1, m2):
    if len(m1) != len(m2): 
        return "To perform matrix substitution, Both length should be equal."
    if len(m1[0]) != len(m2[0]): 
        return  "To perform matrix substitution, Both length should be equal."
    result = []
    for i in range(len(m1)):
        rows = []
        for j in range(len(m1[0])): 
            rows.append(m1[i][j] - m2[i][j])
        result.append(rows)
    return result

def dotProduct(m1, m2):
    # error check 
    if len(m1) != len(m2[0]): 
        return "Can't perform matrix multiplication!"
    result = [[0 for _ in range(len(m1))] for _ in range(len(m2[0]))]
        # loop to iterate over the rows of A
    for i in range(len(m1)): 
        # loop to iterate over the cols of B
        for j in range(len(m2[0])): 
            # loop to iterate over the rows of B
            for k in range(len(m2)): 
                result[i][j] += m1[i][k] * m2[k][j] # now update the result 
    return result # return result 

def matrixOperation(matrix1, matrix2): 
    inp = input("Enter the operator: ")
    if inp == "+": 
        print(sumMatrix(matrix1, matrix2))
    elif inp == "-":
        print(subsMatrix(matrix1, matrix2))
    elif inp == "." or inp == "×" or inp == "*":
        print(dotProduct(matrix1, matrix2))
    else:
        print("Invalid operator")

print("Enter Value for matrix 1")    
matrix1 = takeInp()
print("Enter Value for matrix 2")
matrix2 = takeInp()

matrixOperation(matrix1, matrix2)
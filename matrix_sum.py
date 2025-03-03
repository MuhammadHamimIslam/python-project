rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of columns:"))

def takeInp(rows, cols):
  matrix = []
  for i in range(rows): 
    row = []
    for j in range(cols): 
      row.append(int(input(f"Enter the value in {i}×{j}:")))
    matrix.append(row)
  return matrix 

def sumMatrix(matrix1, matrix2): 
  sumMat = []
  for i in range(len(matrix1)):
    rows = []
    for j in range(len(matrix1[0])): 
     rows.append(matrix1[i][j] + matrix2[i][j])
    sumMat.append(rows)
  return sumMat

print("Enter value for Matrix A")  
A = takeInp(rows, cols)

print("Enter value for Matrix B")
B = takeInp(rows, cols)


C = sumMatrix(A, B)
print(C)

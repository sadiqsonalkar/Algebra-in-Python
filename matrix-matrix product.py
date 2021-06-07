Write a program to do the following: 
•	Find the vector –matrix multiplication of a r by c matrix M with an c-vector u. 
•	Find the matrix-matrix product of M with a c by p matrix N. 


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],"\t",end=" ")
        print("\n")
	
 
m = int(input("Enter the rows for the first matrix::"))
n = int(input("Enter the columns for the first matrix::"))
p = int(input("Enter the rows for the second matrix::"))
q = int(input("Enter the columns for the second matrix::"))
    
if(n!=p):
    print("Matrix multipilication is not possible")
    exit()

	
array1=[[0 for j in range  (0 , n)] for i in range (0 , m)]
array2=[[0 for j in range  (0 , q)] for i in range (0 , p)]
result=[[0 for j in range  (0 , q)] for i in range (0 , m)]
 
print("Enter elements of the first matrix::")
for i in range(0,m):
    for j in range(0,n):
            array1[i][j] = int(input("Enter the element::"))
	
print("Enter elements of the second matrix::")
for i in range(0,p):
    for j in range(0,q):
            array2[i][j] = int(input("Enter the element::"))
	
print("The First Matrix::")
print_matrix(array1)

print("The Second Matrix::")
print_matrix(array2)
	
for i in range(0,m):
    for j in range(0,q):
            for k in range(0,n):
                result[i][j] += array1[i][k] * array2[k][j]
				
print("Multiplication of two matrices::")
print_matrix(result)

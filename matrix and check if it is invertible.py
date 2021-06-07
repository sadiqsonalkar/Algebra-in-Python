def printMatrix(A):
    for i in range(len(A)):
        print(A[i])

def transpose(A):
    T=[[A[i][j] for i in range(len(A))]for j in range(len(A))]
    return T

c=int(input("Enter no. of rows and columns of square matrix:"))
r=c
M=[]
for i in range(r):
   print("Enter elements of row:",i)
   M.append([])
   for j in range(c):
       n=int(input("Enter no.:"))
       M[i].append(n)


print("The entered matrix M1 is:")
printMatrix(M)
determinant=0
if (r==2):
    determinant==M[0][0]*M[1][1]-M[0][1]*M[1][0]
    print("Determinant=",determinant)
    if (determinant==0):
        print("Matrx is not invertible")
    else:
        print("Matrix is invertible")
        CFM=[]
        for i in range(2):
            CFM.append([])
            CFM[0].append(M[1][1])
            CFM[0].append(-(M[0][1]))
            CFM[1].append(-(M[1][0]))
            CFM[1].append(M[0][0])
        print("Cofactor matrix")
        printMatrix(CFM)
        MI=[];
        for i in range(2):
            MI.append([])
            for j in range(2):
                MI.append(CFM.append(CFM[i][j]/determinant))
        print("Inverse of a matrix M is:")
        print(MI)
else:
    for i in range(3):
        determinant=determinant+(M[0][i]*M[1][(i+1)%3]*M[2][(i+2)%3]-M[1][(i+2)%3]*M[2][(i+1)%3]);
    print("Determinant=",determinant)
    if(determinant==0):
        print("Matrix is not invertible")
    else:
        print("Matrix is invertible")
        CFM=[]
        for i in range(3):
            CFM.append([])
            for j in range(3):
                v=(M[(i+1)%3][(j+1)%3]*M[(i+2)%3][(j+2)%3])-(M[(i+1)%3][(j+2)%3]*M[(i+2)%3][(j+1)%3])
                CFM[i].append(v)
        print("Cofactor matrix")
        print(CFM)
        AdjM=transpose(CFM)
        MI=[]
        for i in range(3):
            MI.append([])
            for j in range(3):
                MI[i].append(AdjM[i][j]/determinant)
        print("Inverse of a matrix M is:")
        printMatrix(MI)

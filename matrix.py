1) Enter a r/c matrix 
2) Display the matrix 
3) Display the rows and columns of the matrix
4) Find scalar multiplication for a given scalar value
5) Find transpose of the matrix




rows = int(input("Enter number of rows "))
column=int(input("Enter number of columns:"))
m=[]
for i in range (rows):
    m.append([])
    for j in range(column):
        e=int(input("enter element:"))
        m[i].append(e)

def scal(m):
    a=int(input('Enter vaue of a:'))
    unew=[]
    for i in range (rows):
        unew.append([])
        for j in range(column):
            unew[i].append([m[i][j]*a])
    for i in range (rows):
        print(unew[i])

def tran(m):
    rmatrix=[]
    rmatrix = [[0]*rows for i in range(column)];
    for i in range(len(m)):
        for j in range(len(m[0])):
            rmatrix[j][i] = m[i][j]
    for r in rmatrix:
        print (r)

def dis(m):
for i in range(rows):
        print("row",[i])
        print(m[i])
    for i in range(len(m[0])):
        print("column",[i])
        for j in range(len(m)):
            print("[",m[j][i],"]")
ch=True
while ch:
    print("\n1.Display matrix\n2.Display rows and columns\n3.Scalar multiplication\n4.Transpose of matrix\n5.Exit\n")
    ch=int(input("Enter choice:"))

    if ch==1:
        for i in range (rows):
            print(m[i])
    elif ch==2:
        dis(m)
    elif ch==3:
        scal(m)
    elif ch==4:
        tran(m)
    elif ch==5:
        print("Exit")
        ch=False
    else:
        print("\nInvalid Choice")

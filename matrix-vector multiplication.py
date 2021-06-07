Write a program to find matrix-vector multiplication
2. Write a program to find vector-matrix multiplication 


rows = int(input("Enter number of rows "))
column=int(input("Enter number of columns:"))
m=[]
for i in range (rows):
    m.append([])
    for j in range(column):
        e=int(input("enter element:"))
        m[i].append(e)

for i in range (rows):
    print(m[i])

u = []
print('Enter numbers in vector for matrix-vector: ')
um = input("u:")
u=[int(x) for x in um.split()]
print('vector u: ',u)
l=len(u)
print('Matrix-Vector multiplication:')
for i in range (rows):
    res=0
    for j in range(l):
        C=m[i][j]*u[j]
        res=res+C
    print('[',res,']') 
v=[]
print('Enter numbers in vector for vector-matrix:')
vm = input("v:")
v=[int(x)for x in vm.split()]
print('vector v: ',v)
n=len(v)
print('Vector-Matrix multiplication:')
for i in range (column):
    re=0
    for j in range(n):
        D=m[j][i]*v[j]
        re=re+D
    print('[',re,']')

1. Enter a vector u as n-list
2. Enter a vector v as m-list
3. Add both vectors
4. Subtract both vectors
5. Find the au+bv for different values of u and v(scalar multiplication)
6. Find dot product of u and v
 Code:-
from operator import add
from operator import sub
u=list()
n=int(input("ënter the number element in vector"))
print("ënter the the number in vector:")
for i in range(int(n)):
    ul=int(input("u:-"))
    u.append(int(ul))
    print("vector  u:",u)
    v=list()
    m=int(input("enter the numberof element:"))
    print("ente rnumber in vector 2:-")
    for i in range(int(m)):
        v1=int(input("v:"))
        v.append(int(v1))
        print("vector v:",v)

d=0

def addi(u,v):
    print("addition:",(list(map(add,u,v))))
    
def subt(u,v):
    print("subtraction",(list(map(sub,u,v))))

def aubv(u,v):
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    unew=list()
    vnew=list()
    unew=[i*a for i in u]
    vnew=[i*b for i in v]

    print('au+bv:',(list(map(add,unew,vnew))))


def dotp(u,v):
    d=sum(i*j for i,j in zip(u,v))
    print("dot product is",d)

ch=True
while ch:
              print("menu driven")
              print("1.ädd")
              print("2.sub")
              print("3. scalar mul")
              print("4.dot p")
              print("5.exit")
              ch=int(input("ënter the  chioce:"))

              if ch==1:
                  addi(u,v)
              elif ch==2:
                  subt(u,v)
              elif ch==3:
                  aubv(u,v)
              elif ch==4:
                  dotp(u,v)
              elif ch==5:
                  print("exiting")
                  ch=False
              else:
                  print("ïnvaild choice !!!!!!!!!")

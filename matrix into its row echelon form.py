def ToReducedRowEchelonForm(M):
    if not M: return
    lead=0
    rowCount=len(M)
    columnCount=len(M[0])
    for r in range(rowCount):
        if lead>=columnCount:
            return
        i=r
        while M[i][lead]==0:
            i+-1
            if i==rowCount:
                i=r
                lead+=1
                if columnCount==lead:
                    return
        M[i],M[r]=M[r],M[i]
        lv=M[r][lead]
        M[r]=[mrx/float(lv)for mrx in M[r]]
        for i in range(rowCount):
            if i!=r:
                lv=M[i][lead]
                M[i]=[iv-lv*rv for rv,iv in zip(M[r],M[i])]
        lead+=1

def mat():
    a=[]
    b=[]
    n=int(input("\nEnter number of rows:"))
    m=int(input("Enter number of columns:"))
    print("Enter matrix elements:")
    for j in range(n):
        a.append([])
        for i in range(m):
            k=int(input("Enter element for row "+str(j)+":"))
            a[j].append(k)
    print("\nMatrix is : ",a)
    ToReducedRowEchelonForm(a)
    print("\nRow Echelon Form is :")
    for rw in a:
        print(','.join((str(rv) for rv in rw)))

mat()


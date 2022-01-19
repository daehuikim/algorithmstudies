def div(n):
    nlist=[]
    while n>1:
        i=2
        for i in range(2,n+1):
            if n%i==0:
                nlist.append(i)
                n=int(n/i)
                break
            
    return nlist

resultlist=[]
n = int(input())

resultlist=div(n)
sorted(resultlist)

for r in resultlist:
    print(r)
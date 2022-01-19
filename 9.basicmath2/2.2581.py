def isprime(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n>2:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
    
m =int(input())
n =int(input())
primelist=[]

for i in range(m,n+1):
    if isprime(i):
        primelist.append(i)

if len(primelist)==0:
    print(-1)
else:
    print(sum(primelist))
    print(primelist[0])

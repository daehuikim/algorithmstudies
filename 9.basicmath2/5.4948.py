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
    
while True:
    count=0
    n = int(input())
    if n==0:
        break
    for i in range(n,2*n+1):
        if isprime(i):
            count+=1
    print(count)
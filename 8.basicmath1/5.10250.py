t= int(input())

for i in range(t):
    h,w,n=map(int,input().split())
    
    number = n//h+1
    f=n%h
    if f == 0:
        number=n//h
        f = h
    print(f*100+number)
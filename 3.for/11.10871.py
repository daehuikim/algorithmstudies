n,x = map(int,input().split())
numberlist = list(map(int, input().split()))

for i in range(n):
    if numberlist[i] < x:
        print(numberlist[i], end = " ")
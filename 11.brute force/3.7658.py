n = int(input())

info=[]
for i in range(n):
    x,y = map(int,input().split())
    info.append((x,y))

count=1
for i in range(len(info)):
    count = 1
    for j in range(len(info)):
        if info[i][0]<info[j][0] and info[i][1]<info[j][1]:
            count+=1
    print(count,end=' ')
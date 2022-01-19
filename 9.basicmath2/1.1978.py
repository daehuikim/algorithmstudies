n = int(input())
nlist = map(int, input().split())
count=0

for num in nlist:
    check = 0
    for d in range(2,num):
        if num % d == 0:
            check=1
            break
    if num == 1:
        check=1
    if check==0:
        count+=1
            
print(count)
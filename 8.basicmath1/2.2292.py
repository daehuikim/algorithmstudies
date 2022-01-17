n = int(input())

count = 1
if n ==1:
    print(1)
else:
    n=n-1
    while n>0:
        n = n - 6*count
        count = count+1
    print(count)
n = int(input())

n5 = 0
while n>=5 and n%3 != 0:
    n5+=1
    n=n-5
    
if n%3!=0:
    print(-1)
else:
    print("5:",n5)
    print("3:",int(n/3))
    print(n5+int(n/3))
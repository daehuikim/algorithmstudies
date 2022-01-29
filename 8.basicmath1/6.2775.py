t = int(input())

for i in range(t):
    k=int(input())
    n=int(input())
    
    floor=[]
    for j in range(1,n+1):
        floor.append(j)
        
    for _ in range(k):
        for j in range(1,n):
            floor[j]+=floor[j-1]
            
    print(floor[len(floor)-1])
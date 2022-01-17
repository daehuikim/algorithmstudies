afterlist=[]

number = int(input())

beforelist = list(map(int,input().split()))
    
for i in range(number):
    afterlist.append(beforelist[i]/max(beforelist)*100)
    
print(sum(afterlist)/len(afterlist))
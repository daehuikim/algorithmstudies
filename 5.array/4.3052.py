leftlist = []
resultlist=[]

for i in range(10):
    number = int(input())
    leftlist.append(str(number%42))
    
for i in leftlist:
    if i not in resultlist:
        resultlist.append(i)
        
print(len(resultlist))
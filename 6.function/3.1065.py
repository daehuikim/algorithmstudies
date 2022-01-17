def hansu(n):
    if n<100:
        return True
    
    nlist = str(n)
    
    for i in nlist:
        if int(nlist[0])-int(nlist[1])==int(nlist[1])-int(nlist[2]):
            return True
        
    else:
        return False
        
number = int(input())
count = 0

for i in range(1,number+1):
    if hansu(i):
        count = count + 1
print(count)

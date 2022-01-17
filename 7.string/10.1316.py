def norepeat(e):
    new = []
    new.append(e[0])
    for i in range(1,len(e)):
        if e[i-1]!=e[i]:
            new.append(e[i])
    return new

def isrepeat(e):
    if len(e)==len(set(e)):
        return True
    elif len(e)!=len(set(e)):
        return False
    
number = int(input())

count=0
for i in range(number):
    line = list(input())
    
    modified = norepeat(line)
    if isrepeat(modified):
        count +=1

print(count)
        
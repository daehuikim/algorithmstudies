word = input()

time = 0
for e in word:
    if ord(e)<83:
        unit = (ord(e)-ord('A'))//3
    elif ord(e) == 83:
        unit = 5
    elif ord(e)>=84 and ord(e)<=86:
        unit = 6
    elif ord(e)>=87 and ord(e)<=90:
        unit = 7
    
    time = time + 3 +unit
    
print(time)


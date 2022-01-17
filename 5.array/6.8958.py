number = int(input())

for i in range(number):
    sum=0
    unit=1
    
    line = list(str(input()))
    
    for e in line:
        if e == 'O':
            sum = sum + unit
            unit = unit + 1
        elif e == 'X':
            unit = 1
    
    print(sum)
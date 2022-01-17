number = int(input())

for i in range(number):
    
    line = list(map(int,input().split()))
    avg = (sum(line)-line[0])/line[0]
    count = 0
    
    for e in line[1:]:
        if e>avg:
            count = count + 1
            
    print('%.3f' %(count/line[0]*100)+'%')
    
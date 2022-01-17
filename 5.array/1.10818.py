number=int(input())

numberList = list(map(int,input().split()))


#비교 기준을 첫 원소로 잡음
minimum = numberList[0]
maximum = numberList[0]

for i in range(number):
    if minimum > numberList[i]:
        minimum = numberList[i]
    
    if maximum < numberList[i]:
        maximum = numberList[i]
        
print(minimum,maximum)
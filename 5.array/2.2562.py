numberList=[]

for i in range(9):
    numberList.append(int(input()))

maximum = numberList[0]
index = 1

for i in range(9):
    if maximum < numberList[i]:
        maximum=numberList[i]
        index = i + 1
        
print(maximum)
print(index)
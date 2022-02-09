card, m = map(int,input().split())
cardlist = list(map(int,input().split()))
resultlist = []

for i in range (len(cardlist)):
    for j in range (1,len(cardlist)):
        if j <= i:
            continue
        for k in range (2,len(cardlist)):
            if k <=j:
                continue
            result = cardlist[i] + cardlist[j] + cardlist[k]
            resultlist.append(result)

value=0
for i in range (len(resultlist)):
    if resultlist[i]>m:
        continue
    else:
        value = max(value,resultlist[i])

print(value)
    
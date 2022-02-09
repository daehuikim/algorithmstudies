n = int(input())

number=1
count=0


while True:
    search = str(number)
    if search.find("666") !=-1:
        count+=1
        
    if count==n:
        break
    
    number+=1
    
print(count)
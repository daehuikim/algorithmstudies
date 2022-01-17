number = int(input())
origin = number

count = 1
while True:
    
    left = number//10 + number%10
    right = left%10
    
    number = (number%10) * 10 + right
    
    if number == origin:
        print(count)
        break
    
    count = count+1
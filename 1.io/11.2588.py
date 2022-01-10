a=int(input())
b=int(input())

first = (b%10) * a
second = ((b%100)//10) * a
third = (b//100) * a
result = first + second*10 + third*100
print(first)
print(second)
print(third)
print(result)
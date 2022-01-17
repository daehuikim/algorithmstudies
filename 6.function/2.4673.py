def d(n):
    number = 0
    for i in str(n):
        number = number + int(i)
    number = number + int(n)
    return number

numberset = set(range(1, 10001))
selfnumberset = set()

for i in range(1,10001):
    if d(i)<=10000:
        selfnumberset.add(d(i))

resultset = sorted(numberset - selfnumberset)

for i in resultset:
    print(i)
    
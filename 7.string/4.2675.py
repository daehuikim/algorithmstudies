number = int(input())

for i in range(number):
    n,st = input().split()

    for s in st:
        print(s*int(n),end='')
    print("")
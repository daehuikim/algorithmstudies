# def isprime(n):
#     if n==1:
#         return False
#     elif n==2:
#         return True
#     elif n>2:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#     return True

def isprime(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n>2:
        for i in range(2,n):
            if n%i==0:
                return False
    return True

m,n = map(int,input().split())

for i in range(m,n+1):
    if isprime(i):
        print(i)

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for e in croa:
    word = word.replace(e,'x')
print(len(word))
alphabetcheck = list(0 for i in range(0,26))
word = input()

word = word.upper()

for i in word:
    alphabetcheck[ord(i)-65] += 1


if alphabetcheck.count(max(alphabetcheck)) != 1:
    print("?")
else:
    print(chr(alphabetcheck.index(max(alphabetcheck))+65))
    
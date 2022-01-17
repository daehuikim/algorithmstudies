
word = input()

alphabetcheck=[-1]*26

for i in range(len(word)):
    if alphabetcheck[ord(word[i])-ord('a')] == -1:
        alphabetcheck[ord(word[i])-ord('a')] = i

for i in alphabetcheck:
    print(i,end=' ')
    
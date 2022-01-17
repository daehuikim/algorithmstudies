numbers = input()
a = 100 * int(numbers[2]) + 10 * int(numbers[1]) + int(numbers[0])
b = 100 * int(numbers[6]) + 10 * int(numbers[5]) + int(numbers[4])

print(max(a,b))
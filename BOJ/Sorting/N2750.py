n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

for i in range(n-1):
    min = numbers[i]
    for j in range(i+1, n):
        if numbers[j] < min:
            numbers[i] = numbers[j]
            numbers[j] = min
            min = numbers[i]

for number in numbers:
    print(number)

            


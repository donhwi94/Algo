n = int(input())
times = list(map(int, input().split()))

times.sort()

sum = 0
total = 0

for time in times:
    sum = sum + time
    total += sum

print(total)
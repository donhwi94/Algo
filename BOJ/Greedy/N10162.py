T = int(input())

timers = [300, 60, 10]
counts = [0, 0, 0]

for timer in timers:
    counts[timers.index(timer)] = T // timer
    T = T % timer

if T != 0:
    print(-1)
else:
    for count in counts:
        print(count, end=" ")
n, m = map(int, input().split())

max_value = 0

for i in range(n):
    card = list(map(int, input().split()))
    
    min_value = min(card)

    max_value = max(max_value, min_value)

print(max_value)


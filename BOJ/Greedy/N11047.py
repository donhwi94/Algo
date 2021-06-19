n, k = map(int, input().split())
coin_types = []
for i in range(n):
    coin = int(input())
    if coin <= k:
        coin_types.append(coin)

count = 0

for i in range(len(coin_types)-1, -1, -1):
    count += int(k / coin_types[i])
    k %= coin_types[i]

    if k == 0:
        break

print(count)




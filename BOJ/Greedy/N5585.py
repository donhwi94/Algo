cost = 1000 - int(input())

coin_types = [500, 100, 50, 10, 5, 1]

count = 0

for coin in coin_types:
    count += cost // coin
    cost = cost % coin

    if cost == 0:
        break

print(count)

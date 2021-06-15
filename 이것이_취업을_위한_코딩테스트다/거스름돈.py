n = 1260 
coins = [500, 100, 50, 10]
count = 0

for i in range(len(coins)):
    coin = coins[i]
    count += n // coin
    remain = n % coin
    n = remain

print(count)

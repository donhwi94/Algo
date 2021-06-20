n = int(input())

distances = list(map(int, input().split())) # 도로의 길이
distances.append(0)
prices = list(map(int, input().split())) # 기름 가격

n_price = prices[0] # 현재 도시의 기름 가격
result = n_price * distances[0]

for i in range(1, len(prices)-1):
    if n_price > prices[i]:
        n_price = prices[i]

    result = result + (n_price * distances[i])

print(result)

  

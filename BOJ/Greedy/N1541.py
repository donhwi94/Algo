formulas = input().split("-")

for i in range(len(formulas)):
    values = list(map(int, formulas[i].split("+")))
    
    sum = 0
    for value in values:
        sum += value
    
    formulas[i] = sum

# print(formulas)

result = formulas.pop(0)

while formulas:
    result -= formulas.pop(0)

print(result)
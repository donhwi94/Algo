"""
1. 끝나는 시간을 오름차순으로 정렬 
2. 끝나는 시간이 같을 경우, 시작하는 시간을 오름차순으로 정렬
"""

n = int(input())
mettings = []

count = 1

for i in range(n):
    metting = list(map(int, input().split()))
    mettings.append(metting)

mettings = sorted(mettings, key=lambda x : (x[1], x[0]))
# print(mettings)

endtime = mettings[0][1]
mettings = mettings[1:]

for metting in mettings:
    if metting[0] >= endtime:
        count += 1
        endtime = metting[1]

print(count)
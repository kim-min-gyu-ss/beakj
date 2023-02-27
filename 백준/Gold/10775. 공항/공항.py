import sys
input = sys.stdin.readline
def dangigi(n):
    if airp[n] == n:
        return n
    airp[n] = dangigi(airp[n])
    return airp[n]

G = int(input())
P = int(input())
airp = [num for num in range(G + 1)]
plane = []
for _ in range(P):
    plane.append(int(input()))
cnt = 0
# print(airp)
for i in plane:
    a = dangigi(i)
    if not a:
        break

    airp[a] = airp[a-1]
    cnt += 1
print(cnt)
import sys
input = sys.stdin.readline

def back(n,lst,aa,bb,cc,dd,money):
    global mn, y_lst

    if money >= mn:
        return

    if n > N:
        # if aa >= a and bb >= b and cc >= c and dd >= d:
        #     if mn > money:
        #         mn = money
        #         y_lst = lst
        return

    if aa >= a and bb >= b and cc >= c and dd >= d:
        if mn > money:
            mn = money
            y_lst = lst
        return

    for i in range(n,N):
        if not visited[i]:
            visited[i] = True
            e,f,g,h,l = yachae[i]
            back(i,lst+[i+1],aa+e,bb+f,cc+g,dd+h,money+l)
            visited[i] = False

N = int(input())
a,b,c,d = map(int,input().split())
yachae = []
for _ in range(N):
    yachae.append(list(map(int,input().split())))
mn = 1000000000
visited = [False for _ in range(N)]
y_lst = []
back(0,[],0,0,0,0,0)

if y_lst:
    print(mn)
    print(*y_lst)
else:
    print(-1)
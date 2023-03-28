def back(n,lst,c_lst):
    global mn, y_lst
    if c_lst[4] >= mn:
        return
    if n == N:
        return
    if c_lst[0] >= a and c_lst[1] >= b and c_lst[2] >= c and c_lst[3] >= d:
        if mn > c_lst[4]:
            mn = c_lst[4]
            y_lst = lst[:]
        return
    for i in range(n,N):
        if not visited[i]:
            visited[i] = True
            c_lst[0] += yachae[i][0]
            c_lst[1] += yachae[i][1]
            c_lst[2] += yachae[i][2]
            c_lst[3] += yachae[i][3]
            c_lst[4] += yachae[i][4]
            lst.append(i+1)
            back(i,lst, c_lst)
            c_lst[0] -= yachae[i][0]
            c_lst[1] -= yachae[i][1]
            c_lst[2] -= yachae[i][2]
            c_lst[3] -= yachae[i][3]
            c_lst[4] -= yachae[i][4]
            lst.pop()
            visited[i] = False
N = int(input())
a,b,c,d = map(int,input().split())
yachae = [list(map(int,input().split()))for _ in range(N)]
mn = 500*N
visited = [False for _ in range(N)]
y_lst = []
c_lst = [0,0,0,0,0]
back(0,[], c_lst)

if y_lst:
    print(mn)
    print(*y_lst)
else:
    print(-1)
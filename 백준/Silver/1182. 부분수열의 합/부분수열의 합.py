N, S = map(int,input().split())
num_list = list(map(int,input().split()))
count = 0
for i in range(1, 1 << N):  # 0부터 시작시 공집합 부터 시작
    hap = []  # 합을 확인할수 있는 임시변수
    for j in range(N):
        if i & (1 << j):
            # 합이 0이 된다면 True 반환
            hap += [num_list[j]]
        # print(hap)
    if sum(hap) == S:
        count += 1
print(count)
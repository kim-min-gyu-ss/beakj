N = int(input())
crane = sorted(list(map(int,input().split())), reverse= True)
M = int(input())
box = sorted(list(map(int,input().split())), reverse= True)
result = 0
# print(crane)
# print(box)
if crane[0] < box[0]:
    print(-1)
elif crane[0] == box[-1]:
    print(M)
else:
    cnt = 0  # 크레인 인덱스
    idx = 0  # 박스 인덱스
    while box:  # 박스 있을때 까지
        if box[idx] > crane[cnt]:  # 박스크기가 현제 크레인보다 큼
            idx += 1   # 박스 인덱스 + 1
            if idx == M:    # 박스가 끝까지 감
                idx = 0
                result += 1
                cnt = 0
        else:
            box.pop(idx) # 옮긴거 제거
            M -= 1  # 박스길이 1 감소
            cnt += 1    # 인덱스 + 1
            if cnt == N:    # 크레인 한바퀴 돌았음
                result += 1 # 시간 + 1
                cnt = 0 # 인덱스 초기화
                idx = 0 # 박스 인덱스 초기화
            if box and idx == M:    # 박스가 끝까지 감
                idx = 0
                result += 1
                cnt = 0
    if cnt:
        result += 1
    print(result)
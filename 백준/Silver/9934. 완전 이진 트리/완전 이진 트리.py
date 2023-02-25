def a(n):   # 중위순회로 값넣기
    global cnt
    if n > 2 ** K - 1:
        return

    a(n * 2)
    tree[n] = num_list[cnt]
    cnt += 1
    a(n * 2 + 1)


K = int(input())
num_list = list(map(int, input().split()))
cnt = 0
tree = [0] * (2 ** K)
a(1)    # 함수실행
q = 1   # while문 실행조건
tmp = 1     # 입력 띄우기 전용
while q < 2 ** K:   # 입력 띄우면서 나오게
    if q == 2 ** tmp:
        print()
        tmp += 1
    print(tree[q], end=' ')
    q += 1
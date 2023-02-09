from collections import deque
a = int(input())
for _ in range(a):
    len_case, txt_count = map(int,input().split())
    case_list = deque(map(int,input().split()))
    count = 0
    while True:
        if case_list[0] != max(case_list):
            if txt_count != 0:
                case_list.append(case_list.popleft())
                txt_count -= 1
            else:
                case_list.append(case_list.popleft())
                txt_count = len(case_list) - 1
        else:
            case_list.popleft()
            txt_count -= 1
            count += 1
        if txt_count < 0:
            print(count)
            break
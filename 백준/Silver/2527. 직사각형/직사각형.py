for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,input().split())
    if (x1 > p2) or (p1 < x2) or (y1 > q2) or (y2 > q1):
        print('d')
    elif (p1 == x2 and q1 == y2) or (p2 == x1 and q2 == y1) or (x1 == p2 and q1 == y2) or (p1 == x2 and y1 == q2):
        print('c')
    elif (y1 == q2 and x1 <= p2 <= p1) or (y1 == q2 and x1 <= x2 <= p1) or (q1 == y2 and x1 <= p2 <= p1) or (q1 == y2 and x1 <= x2 <= p1)\
        or (p1 == x2 and y1 <= y2 <= q1) or (p1 == x2 and y1 <= q2 <= q1) or (x1 == p2 and y1 <= y2 <= q1) or (x1 == p2 and y1 <= q2 <= q1)\
        or(y1 == q2 and x2 <= p1 <= p2) or (y1 == q2 and x2 <= x1 <= p2) or (q1 == y2 and x2 <= p1 <= p2) or (q1 == y2 and x2 <= x1 <= p2)\
        or (p1 == x2 and y2 <= y1 <= q2) or (p1 == x2 and y2 <= q1 <= q2) or (x1 == p2 and y2 <= y1 <= q2) or (x1 == p2 and y2 <= q1 <= q2):
        print('b')
    else:
        print('a')
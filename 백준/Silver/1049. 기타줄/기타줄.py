a, b = map(int,input().split())
money = []
for i in  range(b):
    jul_6, jul_sol = map(int,input().split())
    money.append((jul_6, jul_sol))
money_1 = sorted(money)
money_2 = sorted(money, key= lambda x : x[1])
final = 0
final_1 = 0
final_2 = 0
final_3 = 0
if a < 6:
    if money_1[0][0] > money_2[0][1] * a:
        final = money_2[0][1] * a
    else:
        final = money_1[0][0]
else:
    final_1 += (a // 6) * money_1[0][0] + (a % 6) * money_2[0][1]
    final_2 += ((a // 6) + 1) * money_1[0][0]
    final_3 += money_2[0][1] * a
    final = min(final_1, final_2, final_3)
print(final)
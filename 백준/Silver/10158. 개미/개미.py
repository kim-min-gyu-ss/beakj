w, h = map(int,input().split())
x, y = map(int,input().split())
time = int(input())

new_xt = time % (2 * w)
new_yt = time % (2 * h)

new_x = x + new_xt
new_y = y + new_yt

if new_x > w:
    new_x = w - (new_x - w)
if new_y > h:
    new_y = h - (new_y - h)
if new_x < 0:
    new_x = abs(new_x)
if new_y < 0:
    new_y = abs(new_y)
print(new_x, new_y)

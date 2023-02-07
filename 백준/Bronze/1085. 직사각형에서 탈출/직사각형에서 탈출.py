x,y,w,h = map(int,input().split())
result = min(w-x, h-y, x, y)
print(result)
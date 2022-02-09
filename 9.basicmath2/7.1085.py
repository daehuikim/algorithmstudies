x,y,w,h=map(int,input().split())

east = w-x
north = h-y
west = x
south = y

print(min(east,north,west,south))
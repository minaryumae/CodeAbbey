import math
list = list(raw_input().strip().strip('j').split("+-"))
x = int(list[0])
y = int(list[1])
r = (((x) ** 2) + ((y) ** 2)) ** .5
print r
angle = math.atan(y / x)
if angle < 0:
    angle = 2 * 3.1415926 + angle
    print angle
else:
    print angle
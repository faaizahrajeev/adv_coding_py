add10 = lambda x: (x+10)
add10(11) # 21

mult = lambda x, y: x*y
mult(2, 7) # 14

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]
points2D_new = sorted(points2D, key=lambda x: x[1])
print(points2D_new) # [(5, -1), (1, 2), (15, 1), (10, 4)]

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b)) # [2, 4, 6, 8, 10]

a = [1, 2, 3, 4, 5]
b = filter(lambda x: x%2==0, a)
print(list(b)) # [2, 4]

from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a) # 24
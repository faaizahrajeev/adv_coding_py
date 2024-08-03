# iterator tools
from itertools import product, permutations
a = [1, 2, 3]
b = [4, 5, 6]
prod = product(a, b)
print(list(prod)) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod)) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

a = [1, 2, 3]
perm = permutations(a)
print(list(perm, 2)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# accumulate - returns accumulated sums with each element 
# you can do other operations as well like multiplication - accumulate(a, func=operator.mul)

from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.max)
print(list(acc)) # [1, 2, 3, 4]

# groupby - groups elements based on a key
from itertools import groupby
def smaller_than_3(x):
    return x<3
a = [1, 2, 3, 4]
groupby_obj = groupby(a, key=smaller_than_3)
for key, value in groupby_obj:
    print(key, list(value)) # True [1, 2] False [3, 4]


# count, cycle, repeat
from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break
for i in repeat(1, 4):
    print(i)
# 1 1 1 1


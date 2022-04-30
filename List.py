# 1. Given a list L  and an index i, write code that will create a new
# list the same as L but with element N removed
# def L():
from os import remove


L = ['Azerbaijan','Malaysia','Singapore','Amsterdam','Canada','Makkah','Madinah','Turkey','Paris','Germany']
del L[4]
M = []
for y in L:
    M.append(y)
print(M)

# 2. Given a list L and an index i, write code that will remove element
# N from L, in place (i.e., won’t create a new list)
# For example: L = [a, b, c, d, e, f, g, h],  N = 5  yields [a, b, c, d, e, g, h]
L = ['Azerbaijan','Malaysia','Singapore','Amsterdam','Canada','Makkah','Madinah','Turkey','Paris','Germany']
L.remove('Germany')
print(L)

# 3. Given a list L, write code that will reverse the list.
L = ['Azerbaijan','Malaysia','Singapore','Amsterdam','Canada','Makkah','Madinah','Turkey','Paris','Germany']
L.reverse()
print(L)

# 4. Given a list L , write code that will reverse the list in place
# (i.e. won’t create a new list)
# For example: [1, 2, 3] -> [3, 2, 1]
L = ['Azerbaijan','Malaysia','Singapore','Amsterdam','Canada','Makkah','Madinah','Turkey','Paris','Germany']
L.reverse()
print(L)

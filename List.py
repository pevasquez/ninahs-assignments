# 1. Given a list L  and an index i, write code that will create a new
# list the same as L but with element N removed
# def L():
from os import remove

print("Exercise 1.")
L = ['Azerbaijan', 'Malaysia', 'Singapore', 'Amsterdam', 'Canada', 'Makkah', 'Madinah', 'Turkey', 'Paris', 'Germany']
del L[4]
M = []
for y in L:
    M.append(y)
print(M)

# 2. Given a list L and an index i, write code that will remove element
# N from L, in place (i.e., won’t create a new list)
# For example: L = [a, b, c, d, e, f, g, h],  N = 5  yields [a, b, c, d, e, g, h]
print("\nExercise 2.")
L = ['Azerbaijan', 'Malaysia', 'Singapore', 'Amsterdam', 'Canada', 'Makkah', 'Madinah', 'Turkey', 'Paris', 'Germany']
L.remove('Germany')
print(L)

# 3. Given a list L, write code that will reverse the list.
print("\nExercise 3.")
L = ['Azerbaijan', 'Malaysia', 'Singapore', 'Amsterdam', 'Canada', 'Makkah', 'Madinah', 'Turkey', 'Paris', 'Germany']
L.reverse()
print(L)

# 4. Given a list L , write code that will reverse the list in place
# (i.e. won’t create a new list)
# For example: [1, 2, 3] -> [3, 2, 1]
print("\nExercise 4.")
L = ['Azerbaijan', 'Malaysia', 'Singapore', 'Amsterdam', 'Canada', 'Makkah', 'Madinah', 'Turkey', 'Paris', 'Germany']
L.reverse()
print(L)


# 5. Fill in the implementation of the method remove_element below, so that the following code passes.
# Avoid the use of the list's `remove` method
def remove_element(input_list, index):
    return input_list


print("\nExercise 5.")
L = ['Azerbaijan', 'Malaysia', 'Singapore', 'Amsterdam', 'Canada', 'Makkah', 'Madinah', 'Turkey', 'Paris', 'Germany']
M = ['Azerbaijan', 'Malaysia', 'Singapore', 'Amsterdam', 'Makkah', 'Madinah', 'Turkey', 'Paris', 'Germany']
N = remove_element(L, 4)
M == N or print(f'Error! Element {L[4]} was not removed')


# 6. Fill in the implementation of the method reverse_list below, so that the following code passes.
# Avoid the use of the list's `reverse` method
def reverse_list(input_list):
    return input_list


print("\nExercise 6.")
L = ['Azerbaijan', 'Malaysia', 'Singapore', 'Amsterdam', 'Canada', 'Makkah', 'Madinah', 'Turkey', 'Paris', 'Germany']
M = L[::-1]
N = reverse_list(L)
M == N or print(f'Error! List is not reversed!')

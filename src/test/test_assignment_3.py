from src.main.assignment_3 import question1, question2, question3, question4, question5, question6
import numpy as np

#Question 1
def f(t, y):
    return t - y**2

print(question1(f, 0, 2, 10, 1))
print()

#Question 2
print(question2(f, 0, 2, 10, 1))
print()

#Question 3
a = np.array([[2, -1, 1],
              [1, 3, 1],
              [-1, 5, 4]])
b = np.array([6, 0, -3])
print(question3(a, b))
print()

#Question 4
a = np.array([
    [1, 1, 0, 3],
    [2, 1, -1, 1],
    [3, -1, -1, 2],
    [-1, 2, 3, -1]
    ])

det, L, U = question4(a)
print(det)
print()
print(L)
print()
print(U)
print()

#Question 5
a = np.array([
    [9, 0, 5, 2, 1],
    [3, 9, 1, 2, 1],
    [0, 1, 7, 2, 3],
    [4, 2, 3, 12, 2],
    [3, 2, 4, 0, 8]
])
print(question5(a))
print()

#Question 6
a = np.array([
    [2, 2, 1],
    [2, 3, 0],
    [1, 0, 2]
])
print(question6(a))



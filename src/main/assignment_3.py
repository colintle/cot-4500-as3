import numpy as np

def question1(f, tStart, tEnd, iterations, y0):
    dt = (tEnd - tStart) / iterations

    steps = np.linspace(tStart, tEnd, iterations + 1)
    results = np.zeros(iterations + 1)
    results[0] = y0

    for i in range(iterations):
        results[i + 1] = results[i] + f(steps[i], results[i]) * dt
    
    return results[-1]

def question2(f, tStart, tEnd, iterations, y0):
    dt = (tEnd - tStart) / iterations
    steps = np.linspace(tStart, tEnd, iterations + 1)
    results = np.zeros(iterations + 1)
    results[0] = y0

    for i in range(iterations):
        order1 = f(steps[i], results[i])
        order2 = f(steps[i] + dt/2, results[i] + dt/2 * order1)
        order3 = f(steps[i] + dt/2, results[i] + dt/2 * order2)
        order4 = f(steps[i] + dt, results[i] + dt * order3)
        
        results[i + 1] = results[i] + (dt/6) * (order1 + 2*order2 + 2*order3 + order4)
    
    return results[-1]

def question3(a, b):
    n = len(b)
    
    for i in range(n):
        maximum = abs(a[i][i])
        maxRow = i
        for j in range(i+1, n):
            if abs(a[j][i]) > maximum:
                maximum = abs(a[j][i])
                maxRow = j

        for j in range(i, n):
            a[maxRow][j], a[i][j] = a[i][j], a[maxRow][j]
        b[maxRow], b[i] = b[i], b[maxRow]

        for j in range(i+1, n):
            temp = -a[j][i] / a[i][i]
            for k in range(i, n):
                if i == k:
                    a[j][k] = 0
                else:
                    a[j][k] += temp * a[i][k]
            b[j] += temp * b[i]

    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i] / a[i][i]
        for k in range(i-1, -1, -1):
            b[k] -= a[k][i] * x[i]

    return x

def question4(a):
    n = len(a)
    det = 1
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i, n):
            up = 0
            for k in range(i):
                up += L[i][k] * U[k][j]
            U[i][j] = a[i][j] - up
        
        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                down = 0
                for k in range(i):
                    down += L[j][k] * U[k][i]
                L[j][i] = (a[j][i] - down) / U[i][i]
    
    for i in range(len(U)):
        det *= U[i][i]

    return det, L, U

def question5(a):
    for i in range(len(a)):
        other = 0
        for j in range(len(a[i])):
            if i != j:
                other += abs(a[i][j])
        if abs(a[i][i]) < other:
            return False
    return True

def question6(a):
    for i in range(len(a)):
        sub = a[:i-1, :i-1]
        if np.linalg.det(sub) <= 0:
            return False
    return True


def print_m(A):
    for i in A:
        print(*i, file=fout)
        
def sum_m(A, B, row_A, col_A, row_B, col_B):
    global Flag
    if row_A == row_B and col_A == col_B:
        res = [[0 for col in range(col_A)] for row in range(row_A)]
        for i in range(row_A):
            for j in range(col_A):
                res[i][j] = A[i][j] + B[i][j]
        return res
    else:
        Flag = False
        return

def mult_matrix_on_const(a, A, row_A, col_A):
    res = [[0 for col in range(col_A)] for row in range(row_A)]
    for i in range(row_A):
        for j in range(col_A):
            res[i][j] = a * A[i][j]
    return res

def matrix_mult(A, B, row_A, col_A, row_B, col_B):
    global Flag
    if col_A != row_B:
        Flag = False
        return
    else:
        res = [[0 for col in range(col_B)] for row in range(row_A)]

        for i in range(row_A):
            for j in range(col_B):
                for k in range(col_A):
                    res[i][j] += A[i][k] * B[k][j]
        return res

def tranport_matrix(A, row_A, col_A):
    res = [[0 for col in range(row_A)] for row in range(col_A)]
    for i in range(col_A):
        for j in range(row_A):
            res[i][j] = A[j][i]
    return res, col_A, row_A

fin = open('input1.txt', "r")
fout = open('output1.txt', "w")

a, b = map(float, fin.readline().split())

row_A, col_A = map(int, fin.readline().split())
A1 = list(map(float, fin.readline().split()))
A = []
l = []
for i in range(row_A * col_A):
    l.append(A1[i])
    if i % col_A == col_A - 1:
        A.append(l)
        l = []
    
row_B, col_B = map(int, fin.readline().split())
B1 = list(map(float, fin.readline().split()))
B = []
l = []
for i in range(row_B * col_B):
    l.append(B1[i])
    if i % col_B == col_B - 1:
        B.append(l)
        l = []

row_C, col_C = map(int, fin.readline().split())
C1 = list(map(float, fin.readline().split()))
C = []
l = []
for i in range(row_C * col_C):
    l.append(C1[i])
    if i % col_C == col_C - 1:
        C.append(l)
        l = []

row_D, col_D = map(int, fin.readline().split())
D1 = list(map(float, fin.readline().split()))
D = []
l = []
for i in range(row_D * col_D):
    l.append(D1[i])
    if i % col_D == col_D - 1:
        D.append(l)
        l = []

row_F, col_F = map(int, fin.readline().split())
F1 = list(map(float, fin.readline().split()))
F = []
l = []
for i in range(row_F * col_F):
    l.append(F1[i])
    if i % col_F == col_F - 1:
        F.append(l)
        l = []

Flag = True

def solving(a, b,
            row_A, col_A, A,
            row_B, col_B, B,
            row_C, col_C, C,
            row_D, col_D, D,
            row_F, col_F, F):
    global Flag
    A = mult_matrix_on_const(a, A, row_A, col_A)
    B, row_B, col_B = tranport_matrix(B, row_B, col_B)
    B = mult_matrix_on_const(b, B, row_B, col_B)
    T = sum_m(A, B, row_A, col_A, row_B, col_B)
    if not Flag:
        return 0, 0, 0
    row_T = len(T)
    col_T = len(T[0])
    T, row_T, col_T = tranport_matrix(T, row_T, col_T)
    P = matrix_mult(C, T, row_C, col_C, row_T, col_T)
    if not Flag:
        return 0, 0, 0
    row_P = len(P)
    col_P = len(P[0])
    T = matrix_mult(P, D, row_P, col_P, row_D, col_D)
    if not Flag:
        return 0, 0, 0
    row_T = len(T)
    col_T = len(T[0])
    F = mult_matrix_on_const(-1, F, row_F, col_F)
    RES = sum_m(T, F, row_T, col_T, row_F, col_F)
    if not Flag:
        return 0, 0, 0
    return row_F, col_F, RES

row_J, col_J, J = solving(a, b,
                          row_A, col_A, A,
                          row_B, col_B, B,
                          row_C, col_C, C,
                          row_D, col_D, D,
                          row_F, col_F, F)

if Flag:
    print(1, file=fout)
    print(row_J, col_J, file=fout)
    print_m(J)
else:
    print(0, file=fout)

fin.close()
fout.close()

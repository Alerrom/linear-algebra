def show(array):
    for i in array:
        print(i)

def reflect(ab, n):
    res = [''] * 3
    for i in range(3):
        res[i] = ab[i] - 2.0 * scalar_composition(n, ab) * n[i]

    return res

def scalar_composition(vector_a, vector_b):
    scalar = (vector_a[0] * vector_b[0] +
                vector_a[1] * vector_b[1] +
                vector_a[2] * vector_b[2])
    return scalar

def vector_composition(vector_a, vector_b):
    result = [0.0] * 3
    result[0] = vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1]
    result[1] -= vector_a[0] * vector_b[2] - vector_a[2] * vector_b[0]
    result[2] = vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
    return result

def create_normal_vector(A, B, C):
    bc = create_vector_xy(B, C)
    ba = create_vector_xy(B, A)
    result = vector_composition(bc, ba)
    return result

def create_vector_xy(X, Y):
    res = [Y[i] - X[i] for i in range(3)]
    return res

def vector_summ(ab, ac):
    res = [ab[i] + ac[i] for i in range(3)]
    return res

def opposit_point(ba, bc, B):
    bd = vector_summ(ba, bc)
    D = [bd[i] + B[i] for i in range(3)]
    return D

def create_cube(A, B, C, D):
    ba = create_vector_xy(B, A)
    bc = create_vector_xy(B, C)
    A_1 = opposit_point(ba, bc, B)
    
    cb = create_vector_xy(C, B)
    cd = create_vector_xy(C, D)
    D_1 = opposit_point(cb, cd, C)

    bd1 = create_vector_xy(B, D_1)
    C_1 = opposit_point(ba, bd1, B)

    ca1 = create_vector_xy(C, A_1)
    B_1 = opposit_point(ca1, cd, C)

    return [A, B, C, A_1, C_1, D_1, D, B_1]

# orig и dir задают начало и направление луча. v0, v1, v2 - вершины треугольника.
# Функция возвращает расстояние от начала луча до точки пересечения или 0.
def triangle_intersection(orig, dir, v0, v1, v2):
    e1 = [v1[i] - v0[i] for i in range(3)]
    e2 = [v2[i] - v0[i] for i in range(3)]

    pvec = vector_composition(dir, e2)
    det = scalar_composition(e1, pvec)

    if (not 1e-8>= det <= -1e-8):
        return 0

    inf_det = 1 / det
    tvec = [orig[i] - x0[i] for i in range(3)]
    u = scalar_composition(tvec, pvec) * inv_det
    if (u < 0 or u > 1):
        return 0

    qveq = vector_composition(tvec, e1)
    v = scalar_composition(dir, qvec) * inv_det
    if (v < 0 or u + v > 1):
        return 0
    return scalar_composition(e2, qvec) * inv_det

fin = open('input3.txt')
fout = open('output3.txt', "w")

A = list(map(float, fin.readline().split()))
B = list(map(float, fin.readline().split()))
C = list(map(float, fin.readline().split()))
D = list(map(float, fin.readline().split()))

input_vector = list(map(float, fin.readline().split()))
input_point = list(map(float, fin.readline().split()))

start_energy = int(fin.readline())
n = int(fin.readline())

mirror_data = [[] for i in range(n)]

for i in range(n):
    P_i = list(map(float, fin.readline().split()))
    Q_i = list(map(float, fin.readline().split()))
    R_i = list(map(float, fin.readline().split()))
    
    qp = create_vector_xy(Q_i, P_i)
    qr = create_vector_xy(Q_i, R_i)
    T_i = opposit_point(qp, qr, Q_i)
    
    mirror_data[i].append(P_i)
    mirror_data[i].append(Q_i)
    mirror_data[i].append(R_i)
    mirror_data[i].append(T_i)

cube = create_cube(A, B, C, D)

show(mirror_data)
print(*create_normal_vector(mirror_data[0][0], mirror_data[0][1], mirror_data[0][2]))

fin.close()
fout.close()

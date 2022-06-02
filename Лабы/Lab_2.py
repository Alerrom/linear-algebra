import math

def vector_lengh(vector):
    lengh = (vector[0]**2 +
             vector[1]**2 +
             vector[2]**2)**0.5
    return lengh

def angle_between_vectors(vector_a, vector_b):
    cos_alpha = scalar_composition(vector_a, vector_b)
    cos_alpha /= vector_lengh(vector_a) * vector_lengh(vector_b)
    return round(math.degrees(math.acos(cos_alpha)), 2)

def scalar_composition(vector_a, vector_b):
    scalar = (vector_a[0] * vector_b[0] +
                vector_a[1] * vector_b[1] +
                vector_a[2] * vector_b[2])
    return scalar

def vector_composition(vector_a, vector_b):
    result = [0.0, 0.0, 0.0]
    result[0] = vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1]
    result[1] -= vector_a[0] * vector_b[2] - vector_a[2] * vector_b[0]
    result[2] = vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
    return result
    
#fin = open('input2.txt')
#fout = open('output2.txt', "w")

fin = open('input.txt')
fout = open('output.txt', "w")

ship_radius_vector = list(map(float, fin.readline().split())) + [0.0]
keel_vector = list(map(float, fin.readline().split())) + [0.0]
mast_direction_vector = list(map(float, fin.readline().split())) + [1.0]
enemy_ship_radius_vector = list(map(float, fin.readline().split())) + [0.0]

absciss = [1.0, 0.0, 0.0]
ordinat = [0.0, 1.0, 0.0]
aplicat = [0.0, 0.0, 1.0]

final_words = "Auf_wiedersehen"
ship_side = 0
betta_angle = 1000
mast_angle = 1000

for i in range(3):
    enemy_ship_radius_vector[i] -= ship_radius_vector[i]

right_ship_side_vector = vector_composition(keel_vector, aplicat)
left_ship_side_vector = vector_composition(aplicat, keel_vector)

#check enemy direction
if angle_between_vectors(left_ship_side_vector, enemy_ship_radius_vector) < 90:
    if angle_between_vectors(left_ship_side_vector, enemy_ship_radius_vector) <= 60:
        ship_side = 1
        if 0 < angle_between_vectors(keel_vector, enemy_ship_radius_vector) <= 90:
            betta_angle = angle_between_vectors(left_ship_side_vector, enemy_ship_radius_vector)
        else:
            betta_angle = (-1.0) * angle_between_vectors(left_ship_side_vector, enemy_ship_radius_vector)
elif angle_between_vectors(right_ship_side_vector, enemy_ship_radius_vector) < 90:
    if angle_between_vectors(right_ship_side_vector, enemy_ship_radius_vector) <= 60:
        ship_side = -1
        if angle_between_vectors(keel_vector, enemy_ship_radius_vector) <= 90:
            betta_angle = angle_between_vectors(right_ship_side_vector, enemy_ship_radius_vector)
        else:
            betta_angle = (-1.0) * angle_between_vectors(right_ship_side_vector, enemy_ship_radius_vector)

#check mast angle
if ship_side > 0:
    if angle_between_vectors(right_ship_side_vector, mast_direction_vector) < 90:
        #if angle_between_vectors(aplicat, mast_direction_vector) <= 60:
        mast_angle = angle_between_vectors(aplicat, mast_direction_vector)
    else:
        #if angle_between_vectors(aplicat, mast_direction_vector) <= 60:
        mast_angle = (-1.0) * angle_between_vectors(aplicat, mast_direction_vector)
elif ship_side < 0:
    if angle_between_vectors(left_ship_side_vector, mast_direction_vector) < 90:
        #if angle_between_vectors(aplicat, mast_direction_vector) <= 60:
        mast_angle = angle_between_vectors(aplicat, mast_direction_vector)
    else:
        #if angle_between_vectors(aplicat, mast_direction_vector) <= 60:
        mast_angle = (-1.0) * angle_between_vectors(aplicat, mast_direction_vector)

if abs(ship_side):
    print(ship_side, file=fout)
    if abs(betta_angle) <= 60:
        print(betta_angle, file=fout)
    if abs(mast_angle) <= 60:
        print(mast_angle, file=fout)
    print(final_words, file=fout)
else:
    print(ship_side, file=fout)





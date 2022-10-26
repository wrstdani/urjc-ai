from math import pi

grados = float(input())

def degrees_to_radians(grados):
    return grados * 2 * pi / 360

print(degrees_to_radians(grados))
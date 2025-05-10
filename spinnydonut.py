import math
import time
import os
import sys


# yk that uh spinning donut on lua when u download xeno exec
# yeah i ported that to python xd


a = 0
b = 0

while True:
    z = [0] * 7040
    screen = [" "] * 1760

    j = 0
    while j < 6.28:
        j += 0.07
        i = 0
        while i < 6.28:
            i += 0.02

            sinA = math.sin(a)
            cosA = math.cos(a)
            cosB = math.cos(b)
            sinB = math.sin(b)

            sini = math.sin(i)
            cosi = math.cos(i)
            cosj = math.cos(j)
            sinj = math.sin(j)

            cosj2 = cosj + 2
            mess = 1 / (sini * cosj2 * sinA + sinj * cosA + 5)
            t = sini * cosj2 * cosA - sinj * sinA

            x = int(40 + 30 * mess * (cosi * cosj2 * cosB - t * sinB))
            y = int(12 + 15 * mess * (cosi * cosj2 * sinB + t * cosB))
            o = x + 80 * y

            N = int(8 * ((sinj * sinA - sini * cosj * cosA) * cosB - sini * cosj * sinA - sinj * cosA - cosi * cosj * sinB))
            if 0 <= y < 22 and 0 <= x < 80 and z[o] < mess:
                z[o] = mess
                screen[o] = '.,-~:;=!*#$@'[max(N, 0)]

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    output = ''
    for index in range(len(screen)):
        output += screen[index]
        if index % 80 == 79:
            output += '\n'

    sys.stdout.write(output)
    sys.stdout.flush()

    a += 0.04
    b += 0.02

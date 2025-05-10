import math
import os
import time

a = 0
b = 0

# Longest smooth gradient from light to dark
shades = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/*tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def rotate(x, y, z, a, b):
    sinA, cosA = math.sin(a), math.cos(a)
    sinB, cosB = math.sin(b), math.cos(b)
    
    # Rotate around Y (a) then X (b)
    x2 = cosB * x + sinA * sinB * y - cosA * sinB * z
    y2 = cosA * y + sinA * z
    z2 = sinB * x - sinA * cosB * y + cosA * cosB * z
    return x2, y2, z2

while True:
    screen = [" "] * 1760
    zbuffer = [0] * 1760

    # Increased resolution: 1 degree latitude, 2 degree longitude
    for theta in range(0, 180, 1):  # latitude
        for phi in range(0, 360, 2):  # longitude
            theta_rad = math.radians(theta)
            phi_rad = math.radians(phi)

            # Sphere point (radius = 1)
            x = math.sin(theta_rad) * math.cos(phi_rad)
            y = math.cos(theta_rad)
            z = math.sin(theta_rad) * math.sin(phi_rad)

            # Rotate
            x_rot, y_rot, z_rot = rotate(x, y, z, a, b)
            z_rot += 3  # move away from camera
            ooz = 1 / z_rot
            xp = int(40 + x_rot * 22 * ooz)
            yp = int(12 - y_rot * 11 * ooz)
            idx = xp + yp * 80

            # Lighting based on fixed light direction
            lum = x * 0 + y * 1 + z * -1
            shade_idx = int((lum + 1) * (len(shades) - 1) / 2)

            if 0 <= xp < 80 and 0 <= yp < 22 and ooz > zbuffer[idx]:
                zbuffer[idx] = ooz
                screen[idx] = shades[max(0, min(len(shades) - 1, shade_idx))]

    os.system("cls" if os.name == "nt" else "clear")
    for i in range(0, len(screen), 80):
        print("".join(screen[i:i+80]))

    a += 0.03
    b += 0.02
    time.sleep(0.01)

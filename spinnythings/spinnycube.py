import math
import os
import time

a = 0
b = 0

# More gradient shades for smoother lighting
shades = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/*tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# Define cube faces: center (cx, cy, cz) and normal (nx, ny, nz)
faces = [
    ( 0,  0, -1,  0,  0, -1),  # back
    ( 0,  0,  1,  0,  0,  1),  # front
    ( 0, -1,  0,  0, -1,  0),  # bottom
    ( 0,  1,  0,  0,  1,  0),  # top
    (-1,  0,  0, -1,  0,  0),  # left
    ( 1,  0,  0,  1,  0,  0),  # right
]

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

    for face in faces:
        cx, cy, cz, nx, ny, nz = face

        # HIGH detail: more points with tighter spacing
        for u in range(-15, 16):  # 31 steps
            for v in range(-15, 16):  # 31 steps
                step = 0.07

                # Calculate point on the face based on normal
                if abs(nx) == 1:
                    x = cx
                    y = cy + u * step
                    z = cz + v * step
                elif abs(ny) == 1:
                    x = cx + u * step
                    y = cy
                    z = cz + v * step
                else:
                    x = cx + u * step
                    y = cy + v * step
                    z = cz

                # Rotate and project
                x_rot, y_rot, z_rot = rotate(x, y, z, a, b)
                z_rot += 3.5  # push cube away from camera
                ooz = 1 / z_rot
                xp = int(40 + x_rot * 22 * ooz)
                yp = int(12 - y_rot * 11 * ooz)
                idx = xp + yp * 80

                # Compute rotated normal and luminance
                nxr, nyr, nzr = rotate(nx, ny, nz, a, b)
                lum = nxr * 0 + nyr * 1 + nzr * -1  # light from top-front
                shade_index = int((lum + 1) * (len(shades) - 1) / 2)

                if 0 <= xp < 80 and 0 <= yp < 22 and ooz > zbuffer[idx]:
                    zbuffer[idx] = ooz
                    screen[idx] = shades[max(0, min(len(shades) - 1, shade_index))]

    os.system("cls" if os.name == "nt" else "clear")
    for i in range(0, len(screen), 80):
        print("".join(screen[i:i+80]))

    a += 0.03
    b += 0.02
    time.sleep(0.01)

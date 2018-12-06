import numpy as np
import math
x1, x2 = input("input point x and y\n").split()
a = [float(x1), float(x2)]
print("choose mode\n")
print("1. reflection about y axis")
print("2. reflection about x axis")
print("3. reflection about line y = x")
print("4. Rotation about the origin through a positive angle θ")
print("5. Compression/Expansion in the x -direction with factor k")
print("6. Compression/Expansion in the y -direction with factor k")
print("7. Shear in the x -direction by a factor k")
print("8. Shear in the y -direction by a factor k")
mode = int(input())
if mode == 1:
    print(np.matmul(a,[[-1,0], [0,1]]))
elif mode == 2:
    print(np.matmul(a, [[1, 0], [0, -1]]))
elif mode == 3:
    print(np.matmul(a, [[1, 0], [0, 1]]))
elif mode == 4:
    angle = float(input("input angle: "))
    print(np.matmul(a, [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]))
elif mode == 5:
    k = float(input("input k: "))
    print(np.matmul(a, [[k, 0], [0, 1]]))
elif mode == 6:
    k = float(input("input k: "))
    print(np.matmul(a, [[1, 0], [0, k]]))
elif mode == 7:
    k = float(input("input k: "))
    print(np.matmul(a, [[1, 0], [k, 1]]))
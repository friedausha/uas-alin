import numpy as np

x1, x2, x3 = input("V1 : \n").split()
v1 = [float(x1), float(x2), float(x3)]

x1, x2, x3 = input("V2 : \n").split()
v2 = [float(x1), float(x2), float(x3)]

x1, x2, x3 = input("V3 : \n").split()
v3 = [float(x1), float(x2), float(x3)]

x1, x2, x3 = input("U : \n").split()
u = [float(x1), float(x2), float(x3)]
# print(np.inner(u, v1))
ans1 = np.inner(u, v1)
ans2 = np.inner(u, v2)
ans3 = np.inner(u, v3)
print(str(ans1) + " ," + str(ans2) + " ," + str(ans3))
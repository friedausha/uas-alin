import numpy as np

x1, x2, x3 = input("u1 : \n").split()
u1 = [float(x1), float(x2), float(x3)]

x1, x2, x3 = input("u2 : \n").split()
u2 = [float(x1), float(x2), float(x3)]

x1, x2, x3 = input("u3 : \n").split()
u3 = [float(x1), float(x2), float(x3)]

v1 = u1
v2 = u2 - (np.multiply(np.multiply(np.inner(u2, v1), v1), 1/(pow(np.linalg.norm(v1), 2))))
v3 = u3 - ((np.multiply(np.multiply(np.inner(u3, v1), v1), 1/(pow(np.linalg.norm(v1), 2)))) + \
     (np.multiply(np.multiply(np.inner(u3, v2), v2), 1/(pow(np.linalg.norm(v2), 2)))))

norm1 = np.linalg.norm(v1)
norm2 = np.linalg.norm(v2)
norm3 = np.linalg.norm(v3)

print("q1 = " + str(np.multiply(v1, 1/norm1)))
print("q2 = " + str(np.multiply(v2, 1/norm2)))
print("q3 = " + str(np.multiply(v3, 1/norm3)))
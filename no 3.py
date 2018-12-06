import numpy as np

x1, x2, x3 = input("W1 : \n").split()
w1 = [float(x1), float(x2), float(x3)]

x1, x2, x3 = input("W2 : \n").split()
w2 = [float(x1), float(x2), float(x3)]

x1, x2, x3 = input("W3 : \n").split()
w3 = [float(x1), float(x2), float(x3)]

x1, x2, x3 = input("U : \n").split()
u = [float(x1), float(x2), float(x3)]

ans1 = np.inner(w1, w2)
ans2 = np.inner(w2, w3)
ans3 = np.inner(w1, w3)
print(ans1)
if(ans1 == ans2 == ans3 == 0):
    print("w1, w2, w3 are linearly independent")
    norm1 = np.multiply(w1, 1/np.linalg.norm(w1))
    norm2 = np.multiply(w2, 1/np.linalg.norm(w2))
    norm3 = np.multiply(w3, 1/np.linalg.norm(w3))

    ans1 = np.inner(u, norm1)
    ans2 = np.inner(u, norm2)
    ans3 = np.inner(u, norm3)
    print("u = "+ str(ans1) + str(norm1)+ "+ " + str(ans2) + str(norm2)+ "+ " + str(ans3) + str(norm3))
else:
    print("cannot proceed, not linearly independent")
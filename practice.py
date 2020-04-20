import numpy as np

file2 = "practice1.npy"
with open(file2, 'rb') as f:
    a1 = np.load(f)
    print(a1)
    print(a1==-99)
a1[a1==-99]=0
a1[a1 %3 == 0] = a1[a1 %3 == 0]/3


np.random.seed(123)
a2 = np.random.randint(-10, 30, size=(10, 3) )
a3 = a1.dot(a2)
print(a3)

a4 = a3.reshape((2, 15))
print(a4)

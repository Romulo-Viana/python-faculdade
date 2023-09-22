import numpy as np
a=np.array([1,2,3,4,5,7,2,11])
b=np.array([1,2,3,4,5,7,2,11])
prod=0

for indice, item in enumerate(a):
    prod=prod+(a[indice]*b[indice])

print(prod)

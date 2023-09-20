import numpy as np
from scipy.ndimage import rotate

"""

    anduvo pero dio timeout en codewars

"""

def rectangle_rotation(a, b):
    # eje x = a
    # eje y = b
    #print(a,b)
    maximo = max(a, b)
    arr = np.zeros((maximo*2, maximo*2))
    
    centro = [maximo, maximo]
    bl = np.array([int(centro[0]+a/2), int(centro[1]-b/2)])
    tr = np.array([int(centro[0]-a/2), int(centro[1]+b/2)])
    
    arr[bl[1]:tr[1], tr[0]:bl[0]] = 1
    arr = rotate(arr, angle=45)
    suma = 0
    for x in np.nditer(arr):
        if x > 0.5:
            suma += 1
    return suma

    
print(rectangle_rotation(6,4))
print(rectangle_rotation(30,2))
print(rectangle_rotation(8,6))
print(rectangle_rotation(16,20))

# otro usuario

def rectangle_rotation(a, b):
    print("-" * 30)
    a //= 2**0.5
    print("a: ", a)
    b //= 2**0.5
    print("b: ", b)
    r = (a + 1) * (b + 1) + a * b
    print("r: ", r)

    return r + r % 2 - 1

print(rectangle_rotation(6,4))
print(rectangle_rotation(30,2))
print(rectangle_rotation(8,6))
print(rectangle_rotation(16,20))

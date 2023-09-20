def move_zeros(lst):
    nueva_lista = []
    cant_ceros = 0
    for idx, l in enumerate(lst):
        if l == 0:
            cant_ceros += 1
        else:
            nueva_lista.append(l)
    
    for i in range(cant_ceros):
        nueva_lista.append(0)
    
    return nueva_lista


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])) # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


def move_zeros(lst):
    largo = len(lst)
    nueva_lista = list(filter(lambda x: x != 0, lst))
    return nueva_lista + [0 for _ in range(largo-len(nueva_lista))]

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])) # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


# otro usuario
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 )


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])) # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


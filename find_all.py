from itertools import combinations_with_replacement as cc

def find_all(sum_dig, digs):
    lista2 = list(cc('123456789', digs))
    lista_resultante = list(map(lambda x: int(x), list(filter(lambda x: sum([int(i) for i in x]) == sum_dig, [ ''.join(tupla) for tupla in lista2 ]))))
    return [ len(lista_resultante), min(lista_resultante), max(lista_resultante)  ] if lista_resultante else []
print(find_all(10, 3))

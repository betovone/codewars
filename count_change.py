
from itertools import combinations as cc



def probar_coincidencia(m, suma, money, lista_nro):
    if suma + m < money:
        lista_nro.append(m)
        return probar_coincidencia(m, suma+m, money, lista_nro )
    elif suma + m == money:
        lista_nro.append(m)
        return True, lista_nro
    else:
        return False, lista_nro




def combinarCoin(c, coins, money, lista_combinaciones):
    cant = 0
    suma = c
    lista_nro = [c,]
    for m in sorted(coins):
        coincide, lista_nro = probar_coincidencia(m, suma, money, lista_nro)
        if coincide:
            cant +=1
            lista_combinaciones.append(lista_nro)
            lista_nro = [c,]
            suma = c
        else:
            lista_nro = [c,]
            suma = c
    #print(lista_comb)
    return lista_combinaciones

def count_change(money, coins):
    cant = 0
    # verifico y sumo por cada valor sumado a si mismo si llega a money
    #cant += sum([1 for c in coins if money % c == 0])
    
    lista_combinaciones = []
    
    suma = 0
    for c in coins:
        print("prueba con ", c)
        lista_combinaciones = combinarCoin(c, coins, money, lista_combinaciones)
        
    print(lista_combinaciones)
    return len(lista_combinaciones)

    

#assert count_change(4, [1,2]) ==  3
assert count_change(10, [5,2,3]) == 4
assert count_change(11, [5,7]) == 0
assert count_change(0, [1,2]) == 1


def buscar_prox(lista, indice, es_rango):
    """Esta funcion debe ser recursiva 
        Debe buscar el proximo valor si es mayor en 1 unidad debe volverse 
        a llamar hasta encontrar un nro que no se corresponda con dicha condicion
        y debe retornar el ultimo valor que coincida con la condicion
    

    Args:
        lista (list): lista a buscar
        indice (int): indice del valor de la lista
        es_rango (int): 0 no, 1 si
    """
    if not len(lista) > indice + 1:
        return {
            "valor": lista[-1], 
            "separador": ""
        }
    elif lista[indice+1] == lista[indice] + 1:
        return buscar_prox(lista, indice + 1, 1)
    elif lista[indice+1] > lista[indice] + 1 and es_rango == 0:
        return {
            "valor": lista[indice+1], 
            "separador": ","
        }
    elif lista[indice+1] > lista[indice] + 1 and es_rango == 1:
        return {
            "valor": lista[indice], 
            "separador": "-"
        }
    
    

def solution(args):
    if not isinstance(args, list): raise TypeError("El parametro debe ser una lista")
    args.sort()
    lista_valores = []
    nueva_lista = []
    for idx, valor in enumerate(args):
        if not isinstance(valor, int): raise ValueError("Los valores deben ser numeros enteros")
        if idx == 0: 
            nueva_lista.append( 
                               {
                                   "valor:": valor,
                                   "separador": ""
                               } 
                        )
            lista_valores.append(valor)
            # continue
        r = buscar_prox(args, idx, 0)
        if r["valor"] not in lista_valores:
            nueva_lista.append(r)
            lista_valores.append(r["valor"])
    
    print("EJERCICIO")
    print(args)
    print(nueva_lista)
    
    cadena = ""
    cadena.join([ v["valor"], v["separador"] for v in nueva_lista])
    
        
    
    return nueva_lista

    
if __name__ == '__main__':
    solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
    solution([-3,-2,-1,2,10,15,16,18,19,20])

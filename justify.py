

def cantLetras(linea, pos, cant):
    if linea[pos] != ' ':
        pos -= 1 
        cant += 1
        return cantLetras(linea, pos, cant)
    else:
        return 1 + cant


def nuevaLinea(linea):
    cant_espacios_a_sumar = cantLetras(linea, len(linea)-1, 0)
    
    lp = linea[:cant_espacios_a_sumar*-1].rstrip()
    prox = linea[cant_espacios_a_sumar*-1:]
    
    lista_indices_espacios = [idx for idx, l in enumerate(lp) if l == ' ']
    dic_cant_espacios_indice = { l:0 for l in lista_indices_espacios }
    idx=0
    if len(lista_indices_espacios) > 0:
        for i in range(cant_espacios_a_sumar):
            if idx == len(lista_indices_espacios):
                idx = 0
            dic_cant_espacios_indice[lista_indices_espacios[idx]] += 1
            idx += 1

    nueva_linea = ''
    for idx, l in enumerate(lp):
        if l != ' ':
            nueva_linea += l
        else:
            if idx in dic_cant_espacios_indice:
                nueva_linea += l + ' ' * dic_cant_espacios_indice[idx] 
    
    return nueva_linea, prox

    
    


def justify(text, width):
    desde = 0
    nuevo_texto = ""
    texto = text.replace('\n', ' ')
    prox =''
    
    while len(texto) > 0:
        ancho = width-len(prox)
        linea = prox + texto[desde:ancho]
        prox = ''
        if linea[-1] != ' ':
            if len(texto) > ancho:
                if texto[ancho] != ' ':
                    linea, prox = nuevaLinea(linea)
                    prox = prox.lstrip()            
        else:
            linea = linea.strip()
            indice_primer_espacio = linea.index(' ')
            linea = linea[:indice_primer_espacio] + '  ' + linea[indice_primer_espacio+1:]
        texto = texto[ancho:].lstrip()
        nuevo_texto += linea + '\n'
        
    nuevo_texto = nuevo_texto.rstrip('\n') # saco ultimo \n
        
    return nuevo_texto


    
    
print(justify('123 45 6', 7))

t1 = """En Argentina nací
Tierra del Diego y Lionel
De los pibes de Malvinas
Que jamás olvidaré
No te lo puedo explicar
Porque no vas a entender
Las finales que perdimos
Cuantos años las lloré
Pero eso se terminó
Porque en el Maracaná
La final con los brazucas
La volvió a ganar papá
Muchachos
Ahora nos volvimos a ilusionar
Quiero ganar la tercera
Quiero ser campeón mundial
Y al Diego
Desde el cielo lo podemos ver
Con Don Diego y La Tota
Alentándolo a Lionel
Muchachos
Ahora nos volvimos a ilusionar
Quiero ganar la tercera
Quiero ser campeón mundial
Y al Diego
Desde el cielo lo podemos ver
Con Don Diego y La Tota
Alentándolo a Lionel, y ser campeones otra vez, y ser campeones otra vez.
"""

print(justify(t1, 30))

t2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor."
print(justify(t2, 15))



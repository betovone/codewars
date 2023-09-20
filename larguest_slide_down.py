# no lo pude hacer
def sumar_caminos(pyramid, pos):
    suma = 0
    escalon_pos = 0
    for escalon in pyramid:
        if len(escalon) == 1:
            suma += escalon[0]
            print(escalon[0], end=" ")    
        else:
            print("pos=", pos)
            pos = pos if escalon[pos] > escalon[pos+1] else pos+1
            suma += escalon[pos]
            print(escalon[pos], end=" ")
        
    print(f"resultado={suma}")
    return suma, pos


def longest_slide_down(pyramid):
    lista_sumas = []
    escalon = 0
    pos = 0
    while len(pyramid)-1 > escalon:
        suma, pos = sumar_caminos(pyramid, pos)
        lista_sumas.append(suma)
        escalon += 1
        pyramid = pyramid[escalon:]
        
    print("max listas_suma=", max(lista_sumas))
    return max(lista_sumas)

"""
longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) # 23

longest_slide_down([
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ]) #, 1074)
"""

#otro usuario

def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))] 
        print("res=", res)
    return res.pop()

print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])) # 23

print(
longest_slide_down([
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ])) #, 1074)



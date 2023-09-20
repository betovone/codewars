
from itertools import combinations as cc

def choose_best_sum(t, k, ls):
    if len(ls) < k: return None

    distancia = 0
           
    for c in cc(sorted(list(filter(lambda x: x <= t, ls))), k):
        suma_distancias = sum(c)
        if distancia < suma_distancias <= t:
            distancia = suma_distancias

    return distancia if distancia else None



xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

assert choose_best_sum(230, 4, xs) == 230
assert choose_best_sum(430, 5, xs) == 430
assert choose_best_sum(430, 8, xs) == None

# mejorado
def choose_best_sum(t, k, ls):
    return max([sum(c) for c in cc(list(filter(lambda x: x <= t, ls)), k) if sum(c) <= t], default=None)

assert choose_best_sum(230, 4, xs) == 230
assert choose_best_sum(430, 5, xs) == 430
assert choose_best_sum(430, 8, xs) == None

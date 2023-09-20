
from itertools import permutations as pp, combinations_with_replacement as cc
from decimal import Decimal
import datetime

def medir_tiempos(func):
    def wrapper(n):
        t1 = datetime.datetime.now()
        n2 = func(n)
        t2 = datetime.datetime.now()
        t = t2-t1
        print(f'Tiempo: {t.microseconds} ms')
        return n2
    return wrapper

@medir_tiempos
def next_bigger(n):
    if n < 10: return -1
    nro = str(n)
    while len(str(n)) == len(nro):
        n = n + 1
        if sorted(str(n)) == sorted(nro): return n
    return -1

@medir_tiempos
def next_bigger2(n):
    if n < 10: return -1
    for nro in sorted(pp(str(n))):
        if int(''.join(nro)) > n: return int(''.join(nro))
    return -1
    
@medir_tiempos
def next_bigger3(n):
    if n < 10: return -1
    nro = str(n)
    while n < int(''.join(sorted(nro, reverse=True))):
        n = n + 1
        if sorted(str(n)) == sorted(nro): return n
    return -1



#assert next_bigger(  9) == -1
#assert next_bigger(  12) == 21
#assert  next_bigger(  21) == -1
#assert next_bigger( 513) ==  531
#assert next_bigger( 144) == 414

assert next_bigger(1234567890) == 1234567908
assert next_bigger2(1234567890) == 1234567908
assert next_bigger3(1234567890) == 1234567908

next_bigger(47689754444)
next_bigger3(47689754444)

next_bigger(9915490083147)
next_bigger3(9915490083147)



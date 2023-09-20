

def rotar(s, str_number, idx):
    lista = []
    lst_number = list(str_number)
    lst_number.pop(idx)
    str_number = ''.join(lst_number)
    for i in range(len(str_number)+1):
        lista.append(str_number[:i] + s + str_number[i:])
    return lista
    
def next_smaller(number):
    str_number = str(number)
    lst_comb = []
    for idx, s in enumerate(str_number):
        print(s)
        lst_comb += rotar(s, str_number, idx)
    print(lst_comb)
    """
    if lst_comb and max(lst_comb) < number:
        return max(lst_comb)
    else:
        return -1
    """
    
# NO LO PUDE HACER


# SOLUCION OTRO USUARIO

def next_smaller(n):
    s = str(n)
    i = next((i for i in range(len(s)-1,0,-1) if s[i-1]>s[i]),len(s))
    j = next((j for j in range(len(s)-1,i-1,-1) if s[i-1]>s[j]),-1)
    s = s[:i-1]+s[j]+(s[i:j]+s[i-1]+s[j+1:])[::-1]
    return [int(s),-1][s[0]=='0' or j<0]

print(next_smaller(907)) # 790
print(next_smaller(531)) # 513
print(next_smaller(135)) # -1
print(next_smaller(2071)) # 2017
print(next_smaller(123456798)) # 123456789


# otro usuario

def f(s):
    if ''.join(sorted(s)) == s:
        return ''
    ss = s[1:]
    if ''.join(sorted(ss)) == ss:
        xs = sorted(s, reverse=True)
        next_1st_digit = max(x for x in set(xs) if x < s[0])
        xs.remove(next_1st_digit)
        return next_1st_digit + ''.join(sorted(xs, reverse=True))
    return s[0] + str(f(ss))
    
def next_smaller(n):
    s = f(str(n))
    return int(s) if s and not s.startswith('0') else -1

print(next_smaller(907)) # 790
print(next_smaller(531)) # 513
print(next_smaller(135)) # -1
print(next_smaller(2071)) # 2017
print(next_smaller(123456798)) # 123456789


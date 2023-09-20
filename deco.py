
def nine(arg=None):
    if arg is None:
        return '9'
    else:
        return eval('9' + str(arg))


def five(arg=None):
    if arg is None:
        return '5'
    else:
        return eval('5' + str(arg))

    
def suma(valor):
    return '+' + str(valor)

def resta(valor):
    return '-' + str(valor)

#print(nine())
#print(suma(nine()))

print("9+9=", nine( suma(nine()) )   )
print("9-9=", nine( resta(nine()) )   )

print("5-9=", five( resta(nine()) ))  
print("5+9=", five( suma(nine()) ))  
print("9+5=", nine( suma(five()) ))  

print("9-5=", nine( resta(five()) ))  

print("5+9-5=", five(suma(nine( resta(five()) ))  ))
print("9+5+9-5=", nine(suma(five(suma(nine( resta(five()) ))  ))))



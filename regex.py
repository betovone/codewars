import re

def validar_clave(clave):
    exp_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{6,}$"
    return re.search(exp_reg, clave)

print(validar_clave("fjd8vIR8v"))
print(validar_clave("fj3IR9.;"))
print(validar_clave("fj3I..,,.R9"))


#otra solucion
from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)

print(re.search(regex, "fjd8vIR8v"))
print(re.search(regex, "fj3IR9.;"))
print(re.search(regex, "fj3I..,,.R9"))


# otra

regex = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)

print(re.search(regex, "fjd8vIR8v"))
print(re.search(regex, "fj3IR9.;"))
print(re.search(regex, "fj3I..,,.R9"))

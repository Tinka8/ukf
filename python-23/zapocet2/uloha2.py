# Napíšte program, ktorý načíta dve čísla oddelené na vstupe medzerou, zistí ich rozdiel a súčin.
# Ak je niektoré z čísel záporné, vypíšte "Záporné nerátam".
# Ak niektoré z čísel nie je číslo, vypíšte text: "Zle zadané 1. číslo" alebo "Zle zadané 2. číslo".#
#
# Vstup: 1 5
# Výstup:
# 6
# 5
#
# Vstup: 1 5a7
# Výstup: Zle zadané 2. číslo
#
# Vstup: -1 5
# Výstup: Záporné nerátam

user_input = "1 5".split(" ")

a = user_input[0]
b = user_input[1]

try:
    a = int(a)
except TypeError:
    print("Zle zadané 1. číslo")
    exit()

try:
    b = int(b)
except TypeError:
    print("Zle zadané 2. číslo")
    exit()
print(a)
print(type(a))

    
if a < 0 or b < 0:
    print("Záporné nerátam")
else:
    print(a + b)
    print(a * b)

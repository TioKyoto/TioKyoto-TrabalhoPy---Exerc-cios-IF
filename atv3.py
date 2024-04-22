import math
numero = int(input("informe um número real: "))
if numero >= 0:
    raiz = math.sqrt(numero)
    print(raiz)
else:
    quadrado = numero ** 2
    print(quadrado)


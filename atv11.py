import math
numero = int(input("digite um número inteiro: "))
if numero < 0:
    print("número inválido")
else:
    logaritmo = math.log(numero)
    print(f"o logaritmo de {numero} é:", logaritmo)

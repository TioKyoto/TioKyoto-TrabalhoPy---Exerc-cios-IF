import math
numero = int(input("informe um número real: "))
if numero >= 0:
    raiz = math.sqrt(numero)
    quadrado = numero ** 2
    print(f"a raiz quadrada do numero {numero} é {raiz:.2f}, e o quadrado do número {numero} é {quadrado}")
else:
    print("o numero é invalido")
n1 = float(input("informe um número: "))
n2 = float(input("informe um segundo número: "))

if n1 > n2:
    dif = n1 - n2
    print(f"o primeiro valor é maior e a diferença entre eles é {dif}")
elif n2 > n1:
    dif = n2 - n1
    print(f"o segundo valor é maior e a diferença entre eles é {dif}")
else:
    print('os valores são iguais!')

n1 = int(input('informe o primeiro numero: '))
n2 = int(input('informe o segundo numero: '))
if n1 > n2: 
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print('os valores são iguais!')
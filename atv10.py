numero = int(input("digite um número inteiro maior do que zero: "))
if numero <= 0:
    print("número inválido")
else:
    soma = sum(int(digito) for digito in str(numero))
    print("a soma dos algarismos é:", soma)

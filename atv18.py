numero = int(input('informe um numero inteiro: '))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} é divisível por 3 e por 5.")
elif numero % 3 == 0:
    print(f"{numero} é divisível por 3, mas não por 5.")
elif numero % 5 == 0:
    print(f"{numero} é divisível por 5, mas não por 3.")
else:
    print(f"{numero} não é divisível por 3 nem por 5.")

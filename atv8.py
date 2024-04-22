nota1 = float(input('informe sua primeira nota: '))
nota2 = float(input('informe sua segunda nota: '))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('nota inválida!')
else:
    media = (nota1 + nota2) / 2
    print('sua média é: ', media)

    
nota1 = float(input("informe a nota da prova 1: "))
nota2 = float(input("informe a nota da prova 2: "))
peso1 = 1
peso2 = 2
peso_nota1 = nota1 * peso1
peso_nota2 = nota2 * peso2
media = (peso_nota1 + peso_nota2) / (peso1 + peso2)
print(f"sua média foi: {media:.2f}")
if media > 7.0:
    print('você foi aprovado!')
else: 
    print('você foi reprovado!')

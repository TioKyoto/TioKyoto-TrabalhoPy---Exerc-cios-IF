nota1 = float(input("informe a nota do trabalho de laboratório: "))
nota2 = float(input("informe a nota da avaliação semestral: "))
nota3 = float(input("informe a nota do exame final: "))
peso1 = 2
peso2 = 3
peso3 = 5
peso_nota1 = nota1 * peso1
peso_nota2 = nota2 * peso2
peso_nota3 = nota3 * peso3
media = (peso_nota1 + peso_nota2 + peso_nota3) / (peso1 + peso2 + peso3)
print(f"sua média foi {media:.2f}")
if media >= 0 and media <= 2.9:
    print("você está reprovado!")
elif media >= 3 and media <= 4.9:
    print('você está de recuperação!')
else:
    print("você foi aprovado!")

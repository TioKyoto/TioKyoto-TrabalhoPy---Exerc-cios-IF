sal = float(input("informe o seu salario: "))
emprest = float(input("informe o valor da prestação: "))
porcentagem_salalario = sal * 0.2
if emprest > porcentagem_salalario:
    print("emprestimo não concedido!")
else: 
    print("emprestimo concedido!")

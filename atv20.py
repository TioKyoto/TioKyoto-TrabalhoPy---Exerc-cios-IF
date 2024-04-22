idade = int(input("Informe sua idade: "))
temp_serv = int(input("Informe seu tempo de serviço: "))

if idade > 65 or temp_serv > 30:
    print("Você pode se aposentar!")
elif idade > 60 and temp_serv > 25:
    print("Você pode se aposentar!")
else:
    print("Você não pode se aposentar!")

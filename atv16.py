print("calcule a area de um trapézio")
bmaior = float(input("informe a base maior: "))
bmenor = float(input('infoerma a base maior: '))
altura = float(input("informe a altura: "))
if bmaior >0 and bmenor >0:
    area = (bmaior + (bmenor * altura )) / 2
    print(f"`{area:.2f}")
else:
    print('valor inválido')

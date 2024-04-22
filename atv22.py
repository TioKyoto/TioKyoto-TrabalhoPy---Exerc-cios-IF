valor = float(input("informe o valor do produto: "))
estado = input("informe o estado que sera enviado o produto: ")
match estado:
    case "mg":
        imp = valor * 0.07
        vlr = valor + imp
        print(f"o preoço final do produto é: {vlr:.2f}")
    case "sp":
        imp = valor * 0.12
        vlr = valor + imp
        print(f"o preoço final do produto é: {vlr:.2f}")
    case "rj":
        imp = valor * 0.15
        vlr = valor + imp
        print(f"o preoço final do produto é: {vlr:.2f}")
    case "ms":
        imp = valor * 0.08
        vlr = valor + imp
        print(f"o preoço final do produto é: {vlr:.2f}")
    case _:
        print("Alerta de erro!!")

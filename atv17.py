print("""você possui as seguintes opções de operações:
+
-
/
*""")
operação = input("informe a operação desejada: ")

valor1 = float(input("informe o primeiro valor: "))
valor2 = float(input("informe o segundo valor: "))

match operação:
    case "+": 
        result = valor1 + valor2
        print(result)
    case "-":
        result = valor1 - valor2
        print(result)
    case "/":
        result = valor1 / valor2
        print(f"{result:.2f}")
    case "*":
        result= valor1 * valor2
        print(result)
    
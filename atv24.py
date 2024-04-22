chegada_hora, chegada_minuto = map(int, input("Digite a hora e o minuto de chegada (formato HH MM): ").split())
partida_hora, partida_minuto = map(int, input("Digite a hora e o minuto de partida (formato HH MM): ").split())
diferenca_horas = partida_hora - chegada_hora
if partida_minuto > chegada_minuto:
    diferenca_horas += 1
if diferenca_horas <= 2:
    preco = diferenca_horas * 1.00
elif diferenca_horas <= 4:
    preco = 2 + (diferenca_horas - 2) * 1.40
else:
    preco = 4.80 + (diferenca_horas - 4) * 2.00

print(f"O preço cobrado pelo estacionamento é R$ {preco:.2f}")

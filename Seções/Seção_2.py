print("Bem vindo a calculadora de gorjetas")

# Convertendo as entradas para números
total = float(input("Quanto foi a conta total? R$"))
gorjeta = int(input("Quanto de gorjeta gostaria de dar? 0, 10, 20, 30, 40: "))
quant_pessoas = int(input("Quantas pessoas vão pagar a comida?"))

# Calculando a gorjeta como porcentagem do total
gorjeta_valor = total * (gorjeta / 100)

# Calculando o total com a gorjeta incluída
total_com_gorjeta = total + gorjeta_valor

# Dividindo o total pela quantidade de pessoas
final = total_com_gorjeta / quant_pessoas

# Exibindo o resultado formatado
print(f"Cada pessoa terá que pagar: R${final:.2f}")
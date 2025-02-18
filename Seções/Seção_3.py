print("Jogo do tesouro")
print("Sua missão é achar o tesouro.")
direcao = input("Para qual lado você deseja ir? Direita ou Esquerda")
if direcao == "direita":
    print("Você caiu em um buraco e morreu. Game over")
else:
    print("Você chegou em um lago. Tem uma ilha no meio do lago.")
    direcao2 = input("Digite 'espere' para esperar o barco. Digite 'nadar' para nadar para o outro lado ")
    if direcao2 == "nadar":
        print("Uma truta brava te atacou. Game over")
    else:
        escolha3 = input("Você chegou na ilha sem nenhum equipamento. Tem uma casa com 3 portas. Uma vermelha, uma amarela e outra azul. Qual cor você escolhe? ")
        if escolha3 == "vermelho":
            print("Esse quarto está cheio de fogo. Game over")
        elif escolha3 == "amarela":
            print("Esse quarto está cheio de monstros. Game over")
        elif escolha3 == "azul":
            print("Você achou o tesouro!!! Parabéns!!")
        else:
            print("Você escolheu uma porta inexistente")
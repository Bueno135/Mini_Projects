#Pedra, papel e tesoura jogo

import random

robo = random.randint(1,3)

print("Bem vindo ao jogo do pedra, papel e tesoura")
escolha = input("Escolha 'pedra', 'papel' ou 'tesoura': ")

if robo == 1:
    robo = "pedra"
elif robo == 2:
    robo = "papel"
else:
    robo = "tesoura"

print("robo escolheu: " + robo)
if escolha == "pedra" and robo == "tesoura":
    print("Você ganhou")
elif escolha == "pedra" and robo == "papel":
    print("Você perdeu")
elif escolha == "pedra" and robo == "pedra":
    print("Empate!!")
elif escolha == "tesoura" and robo == "papel":
    print("Você ganhou")
elif escolha == "tesoura" and robo == "pedra":
    print("Você perdeu")
elif escolha == "tesoura" and robo == "tesoura":
    print("Empate!!")
elif escolha == "papel" and robo == "pedra":
    print("Você ganhou")
elif escolha == "papel" and robo == "tesoura":
    print("Você perdeu")
elif escolha == "papel" and robo == "papel":
    print("Empate!!")
    
      
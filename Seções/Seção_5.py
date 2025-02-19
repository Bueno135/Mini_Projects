#you have to make a password generator with random letters, numbers and symbols.
import random

senha = ""

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A','B','C','D','E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '&', '*']

print("Bem vindo ao gerador de senhas!")
nr_letters = int(input("Digite a quantidade de letras da senha desejada: "))
nr_numbers = int(input("Digite a quantidade de números da senha desejada: "))
nr_symbols = int(input("Digite a quantidade de símbolos da senha desejada: "))


for i in range(nr_letters):
    senha += random.choice(letters)
    
for i in range(nr_numbers):
    senha += random.choice(numbers)
    
for i in range(nr_symbols):
    senha += random.choice(symbols)
    
print(senha)
import random

resposta = random.randint(1, 100)


print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")

while True:
    palpite = int(input("Digite um número: "))
    

    if palpite == resposta:
        print(f"Parabéns! Você acertou o número")
        break
    elif palpite < resposta:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")






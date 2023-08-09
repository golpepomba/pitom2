import random

def dado():
    dado = random.randint(1, 6)
    return dado

dado1 = dado()
dado2 = dado()

print("Dado 1: ",dado1)
print("Dado 2: ",dado2)

soma= dado1+dado2

print("A soma dos dois dados é: " ,soma)

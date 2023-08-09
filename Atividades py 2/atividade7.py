def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

try:
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    if numero < 0:
        print("O número não deve ser negativo.")
    else:
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é: {resultado}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro.")

try:
    entrada = input("Digite uma sequência de números separados por espaço: ")
    numeros = [int(numero) for numero in entrada.split()]

    if numeros:
        maior_numero = max(numeros)
        menor_numero = min(numeros)
        print(f"O maior número é: {maior_numero}")
        print(f"O menor número é: {menor_numero}")
    else:
        print("Sequência vazia. Nenhum número encontrado.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números separados por espaço.")

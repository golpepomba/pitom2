def ordenar_lista_crescente(lista_numeros):
    return sorted(lista_numeros)

try:
    entrada = input("Digite uma lista de números separados por espaço: ")
    lista_numeros = [float(numero) for numero in entrada.split()]

    lista_ordenada = ordenar_lista_crescente(lista_numeros)
    print("Lista ordenada de forma crescente:", lista_ordenada)
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números separados por espaço.")

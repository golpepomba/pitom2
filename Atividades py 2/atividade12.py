def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    meio = len(lista_ordenada) // 2
    return (lista_ordenada[meio] + lista_ordenada[~meio]) / 2

entrada = input("Digite uma lista de números separados por espaço: ")
lista_numeros = [int(numero) for numero in entrada.split()]

mediana = calcular_mediana(lista_numeros)
print(f"A mediana dos valores é: {mediana}")

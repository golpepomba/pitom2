def converter(lista_strings):
    return [palavra.upper() for palavra in lista_strings]

try:
    entrada = input("Digite uma lista de palavras separadas por espaço: ")
    lista_strings = entrada.split()

    nova_lista_maiusculas = converter(lista_strings)
    print(nova_lista_maiusculas)
except Exception as e:
    print("Ocorreu um erro:", e)
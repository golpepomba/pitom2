try:
    entrada = input("Digite uma lista de palavras separadas por espaço: ")
    lista_palavras = entrada.split()

    if lista_palavras:
        maior_palavra = max(lista_palavras, key=len)
        menor_palavra = min(lista_palavras, key=len)
        print(f"A maior palavra é: {maior_palavra}")
        print(f"A menor palavra é: {menor_palavra}")
    else:
        print("Lista vazia. Nenhuma palavra encontrada.")
except:
    print("Ocorreu um erro ao processar a lista de palavras:", )

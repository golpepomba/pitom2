def contar_palavras(texto):
    palavras = texto.lower().split()
    return {palavra: palavras.count(palavra) for palavra in set(palavras)}

texto = input("Digite um texto: ")
resultado = contar_palavras(texto)

print("Quantidade de ocorrências de cada palavra:")
for palavra, quantidade in resultado.items():
    print(f"{palavra}: {quantidade}")
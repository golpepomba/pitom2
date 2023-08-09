def palindromo(palavra):
    return palavra == palavra[::-1]


word= input("Digite uma palavra: ")
if palindromo(word):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")

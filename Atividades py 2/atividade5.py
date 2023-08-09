def numeros_pares():
    numeros = input("Digite uma lista de numeros separados por espaço: ")
    return[int(numero) for numero in numeros.split() if int(numero) %2 == 0]

pares = numeros_pares()

print("Números pares :" ,pares)